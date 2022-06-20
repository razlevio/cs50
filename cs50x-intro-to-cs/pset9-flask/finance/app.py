import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, current_price_lookup, quote_lookup, usd, format_numbers

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """ Show the user portfolio of stocks """

    if request.method == "GET":
        # Gathering relevant information about the user and his portfolio
        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?;", user_id)[
            0]["cash"]
        total_portfolio_value = cash
        holdings = db.execute(
            "SELECT * FROM holdings WHERE user_id = ?;", user_id)
        portfolio = []

        # Traversing all of the user holdings and add every holding position to the user portfolio
        for holding in holdings:
            symbol = holding["symbol"]
            current_stock_data = lookup(symbol)
            name = holding["name"]
            shares = holding["number_of_shares"]
            price = current_stock_data["latestPrice"]
            total_value = shares * price
            portfolio.append({
                "symbol": symbol,
                "name": name,
                "shares": shares,
                "price": usd(price),
                "total": usd(total_value),
            })
            # Adding every purchase total cost to the total holdings of the user portfolio
            total_portfolio_value += total_value

        cash = usd(cash)
        total_portfolio_value = usd(total_portfolio_value)

        # Returning the index that present the user portfolio information
        return render_template("index.html", portfolio=portfolio, cash=cash, total_portfolio_value=total_portfolio_value)

        """ Add funds to the account """
    else:
        user_id = session["user_id"]
        user_cash = db.execute("SELECT cash FROM users WHERE id=?;", user_id)[
            0]["cash"]
        amounts = [10000, 20000, 30000]
        selected_amount = float(request.form.get("funds"))
        if selected_amount not in amounts:
            apology("you can't add this amount of funds", 400)
        user_cash += selected_amount
        db.execute("UPDATE users SET cash=? WHERE id=?", user_cash, user_id)
        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        username = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(username) != 1 or not check_password_hash(username[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = username[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure the username is not already exists
        user_exists = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(user_exists) == 1:
            return apology("username already exists", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation password", 400)

        # Ensure that confirmation password and password both the same
        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("password and confirmation password needs to be the same", 400)

        # INSERT the new user into users, storing a hash of the user’s password, not the password itself.
        # Hash the user’s password with generate_password_hash
        hashed_password = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                   request.form.get("username"), hashed_password)

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrive the stock symbol inserted by the user
        stock_symbol = request.form.get("symbol").strip().upper()

        # Ensure symbol was submitted
        if not stock_symbol:
            return apology("must provide stock symbol name", 400)

        # Ensure the stock symbol provided exists
        stock_data = quote_lookup(stock_symbol)
        if not stock_data:
            return apology("the stock symbol provided not exists or we having problem retrive the data right now", 400)

        # Redirect user to present the information about the stock
        return render_template("quoted.html", stock_data=stock_data)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrive the stock symbol inserted by the user
        stock_symbol = request.form.get("symbol").strip().upper()
        shares_number = request.form.get("shares")

        # Ensure symbol was submitted
        if not stock_symbol:
            return apology("must provide stock symbol name", 400)

        # Ensure number of shares was submitted
        if not shares_number:
            return apology("must provide number of shares you want to buy")

        # Ensure the stock symbol provided exists
        stock_data = lookup(stock_symbol)
        if not stock_data:
            return apology("the stock symbol provided not exists or we having problem retrive the data right now", 400)

        # Ensure that the number of shares inserted is a positive number
        try:
            shares_number = int(shares_number)
            if shares_number < 1:
                return apology("number of shares must be positive integer value", 400)
        except ValueError:
            return apology("you inserted wrong value for number of shares, value must be a positive integer", 400)

        # Extracting relevant data for initating a transaction
        user_id = session["user_id"]
        stock_price = stock_data["latestPrice"]
        total_shares_cost = shares_number * stock_price
        account_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?;", user_id)[0]['cash']
        if total_shares_cost > account_cash:
            return apology("you don't have enough cash to make this purchase", 400)

        # Initiating the transaction and updating the databases

        # Update the new user available cash after initiating the transaction
        updated_account_cash = account_cash - total_shares_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   updated_account_cash, user_id)

        # Inserting the transaction to the transactions database
        db.execute("INSERT INTO transactions (user_id, symbol, price, number_of_shares, total_price) VALUES (?, ?, ?, ?, ?)",
                   user_id, stock_symbol, stock_price, shares_number, total_shares_cost)

        # Updating the holdings in the holdings database
        # Checking if the user already holds some stocks in the stock he just bought
        check_owned_stocks = db.execute(
            "SELECT * FROM holdings WHERE user_id=? AND symbol=?;", user_id, stock_symbol)
        # User don't hold any stocks of that company, so insert into holdings the new transaction
        if len(check_owned_stocks) == 0:
            db.execute("INSERT INTO holdings (user_id, name, symbol, number_of_shares, price, total_price) VALUES (?, ?, ?, ?, ?, ?);",
                       user_id, stock_data["companyName"], stock_symbol, shares_number, stock_price, total_shares_cost)
        # User holds stocks of that company, simply update the number_of_shares and the total price
        else:
            current_shares = db.execute(
                "SELECT number_of_shares FROM holdings WHERE user_id=? AND symbol=?;", user_id, stock_symbol)[0]["number_of_shares"]
            updated_shares = current_shares + shares_number
            updated_total = updated_shares * stock_price
            db.execute("UPDATE holdings SET number_of_shares=?, price=?, total_price=? WHERE user_id=? AND symbol=?;",
                       updated_shares, stock_price, updated_total, user_id, stock_symbol)

        # Gathering the purchase information in a dictonary to pass the data into transaction summary page
        transaction_info = {
            "symbol": stock_symbol,
            "stock_price": usd(stock_price),
            "transaction_cost": usd(total_shares_cost),
            "updated_account_cash": usd(updated_account_cash),
            "shares": shares_number,
        }

        # Rendering the transaction summary page

        # UN COMMENT BELOW IF WANT TO RENDER SUCCUEED PAGE with TRANSACTION SUMMARY
        return render_template("transaction_summary.html", transaction_info=transaction_info)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # Getting the logged-in user id
    user_id = session["user_id"]

    # Extract the symbols and number of shares of each stock that the user holds
    symbols_query = db.execute(
        "SELECT symbol, number_of_shares FROM holdings WHERE user_id=?;", user_id)

    # Creating dictonary for holding the symbol -> num of shares for easier reference later
    holdings = {}
    for symbol in symbols_query:
        holdings[symbol["symbol"]] = symbol["number_of_shares"]

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrive the stock symbol inserted by the user and the amount the user want to sell
        symbol_to_sell = request.form.get("symbol")
        shares_to_sell = request.form.get("shares")

        # Ensure symbol was submitted
        if not symbol_to_sell or symbol_to_sell not in holdings:
            return apology("must select stock symbol", 400)

        # Ensure number of shares was submitted
        if not shares_to_sell:
            return apology("must provide number of shares you want to sell")

        # Ensure that the number of shares inserted is a positive integer and that user not trying to sell more shares than he owns
        try:
            shares_to_sell = int(shares_to_sell)
            if shares_to_sell < 1:
                return apology("number of shares you want to sell must be a positive integer value", 400)
            if shares_to_sell > holdings[symbol_to_sell]:
                return apology("you can't sell more shares than what you own", 400)
        except ValueError:
            return apology("you inserted wrong value for number of shares, value must be a positive integer", 400)

        # Extracting relevant data for initating a transaction
        stock_data = lookup(symbol_to_sell)
        stock_price = stock_data["latestPrice"]
        total_shares_cost = shares_to_sell * stock_price
        account_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?;", user_id)[0]['cash']

        # Initiating the transaction and updating the database accordingly

        # Update the new user available cash after initiating the transaction
        updated_account_cash = account_cash + total_shares_cost
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   updated_account_cash, user_id)

        # Inserting the transaction to the transactions database
        db.execute("INSERT INTO transactions (user_id, symbol, price, number_of_shares, total_price) VALUES (?, ?, ?, ?, ?)",
                   user_id, symbol_to_sell, stock_price, -shares_to_sell, total_shares_cost)

        # Updating the holdings database by updating the number of shares and the total price
        current_shares = db.execute(
            "SELECT number_of_shares FROM holdings WHERE user_id=? AND symbol=?;", user_id, symbol_to_sell)[0]["number_of_shares"]
        updated_shares = current_shares - shares_to_sell
        updated_total = updated_shares * stock_price
        # User sold all of his available stocks, hence delete the record from holdings table
        if updated_shares == 0:
            db.execute(
                "DELETE FROM holdings WHERE user_id=? AND symbol=?;", user_id, symbol_to_sell)
        else:
            db.execute("UPDATE holdings SET number_of_shares=?, price=?, total_price=? WHERE user_id=? AND symbol=?;",
                       updated_shares, stock_price, updated_total, user_id, symbol_to_sell)

        # Gathering the transaction information in a dictonary to pass the data into transaction summary page
        transaction_info = {
            "symbol": symbol_to_sell,
            "stock_price": usd(stock_price),
            "transaction_cost": usd(total_shares_cost),
            "updated_account_cash": usd(updated_account_cash),
            "shares": -shares_to_sell,
        }

        # Rendering the purchase summary page
        return render_template("transaction_summary.html", transaction_info=transaction_info)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("sell.html", symbols=holdings.keys())


@app.route("/history")
@login_required
def history():
    """ Show history of transactions """

    # Getting the logged-in user id
    user_id = session["user_id"]

    # Getting all of the transactions of the logged in user
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id=?", user_id)

    # Traversing the transactions in order to reformat the price and total price for presneting usd formatting
    for transaction in transactions:
        transaction["price"] = usd(transaction["price"])
        transaction["total_price"] = usd(transaction["total_price"])

    # Rendering the template with the transactions information
    return render_template("history.html", transactions=transactions)


""" ADDITIONAL FEATURES THAT CAN ADD IF WANT TO GROW THIS PROJECT
    Allow users to change their passwords.
    Allow users to add additional cash to their account.
    Allow users to buy more shares or sell shares of stocks they already own via index itself, without having to type stocks’ symbols manually.
    Require users’ passwords to have some number of letters, numbers, and/or symbols.
    Implement some other feature of comparable scope. """
