# [Bitcoin Price Index](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/#bitcoin-price-index)

![Bitcoin logo](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/Bitcoin.svg.png)

[Bitcoin](https://en.wikipedia.org/wiki/Bitcoin) is a form of digitial currency, otherwise known as [cryptocurrency](https://en.wikipedia.org/wiki/Cryptocurrency). Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a [blockchain](https://en.wikipedia.org/wiki/Blockchain), to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called `bitcoin.py`, implement a program that:

- Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a `float`, the program should exit via `sys.exit` with an error message.
- Queries the API for the CoinDesk Bitcoin Price Index at [https://api.coindesk.com/v1/bpi/currentprice.json](https://api.coindesk.com/v1/bpi/currentprice.json), which returns a [JSON](https://en.wikipedia.org/wiki/JSON) object, among whose nested keys is the current price of Bitcoin as a `float`. Be sure to catch any [exceptions](https://docs.python-requests.org/en/latest/api/#exceptions), as with code like:

  ```
  import requests

  try:
      ...
  except requests.RequestException:
      ...

  ```

- Outputs the current cost of n Bitcoins in USD to four decimal places, using `,` as a thousands separator.
