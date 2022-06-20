import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.
        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def quote_lookup(symbol):
    """Look up quote for symbol."""
    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return {
            "name": quote["companyName"],
            "symbol": quote["symbol"],
            "price": usd(quote["latestPrice"]),
            "marketcap": "$" + format_numbers(quote["marketCap"]),
            "changeusd": usd(quote["change"]),
            "changepercent": f"{(quote['changePercent']*100):.2f}%",
            "52low": usd(quote["week52Low"]),
            "52high": usd(quote["week52High"]),
            "primaryexchange": quote["primaryExchange"],
        }
    except (KeyError, TypeError, ValueError):
        print("EXCEPTION, may be KeyError | TypeError | ValueError")
        return None


def lookup(symbol):
    """ Look up for pure unformatted data of a stock by searching provided symbol """
    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return quote
    except (KeyError, TypeError, ValueError):
        print("EXCEPTION, may be KeyError | TypeError | ValueError")
        return None

def current_price_lookup(symbol):
    """ Look up symbol current price """
    # Contact API
    try:
        api_key = os.environ.get("API_KEY")
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        quote = response.json()
        return quote["latestPrice"]
    except (KeyError, TypeError, ValueError):
        print("EXCEPTION, may be KeyError | TypeError | ValueError")
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def format_numbers(value):
    """Format numbers as comma seperated."""
    return f"{value:,}"