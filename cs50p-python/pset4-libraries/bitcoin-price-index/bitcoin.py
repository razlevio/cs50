from sys import argv, exit
import requests

""" prompt the user for the amount of bitcoins he wants to buy
    then pull the current bitcoin price by sending request to coindesk API
    then outputting the total price of the requested bitcoins amount
    formatted to 4 decimal points """


def main():
    bitcoin_price = get_current_bitcoin_price()  # getting current bitcoin price
    # validate correct cli argument provided
    amount = validate_cli_argument()
    # calculating the total cost of requested bitcons
    cost = bitcoin_price * amount
    # printing the total cost formatted
    print(f"${cost:,.4f}")


""" validating the provided command-line arguments
    user only allowed to insert one number type command line argument """


def validate_cli_argument():
    if len(argv) == 1:
        exit("Missing command-line argument")
    elif len(argv) != 2:
        exit("Too many command-line arguments")
    try:
        inp = float(argv[1])
    except ValueError:
        exit("Command-line argument is not a number")
    else:
        return inp


""" request current bitcoin price from coindesk API
    if there is any problem with the request it will reported
    if the request succeeded, extract the current usd price in float from the json
    and return the current bitcoin price """


def get_current_bitcoin_price():
    try:
        req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except (requests.RequestException, requests.ConnectionError, requests.HTTPError):
        print("Error with the request")
        exit()
    else:
        bitcoin_json = req.json()
        return bitcoin_json.get("bpi").get("USD").get("rate_float")


if __name__ == "__main__":
    main()
