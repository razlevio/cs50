# [C$50 Finance](https://cs50.harvard.edu/x/2022/psets/9/finance/#c50-finance)

Implement a website via which users can “buy” and “sell” stocks, a la the below.

![C$50 Finance](https://cs50.harvard.edu/x/2022/psets/9/finance/finance.png)

## Background

If you’re not quite sure what it means to buy and sell stocks (i.e., shares of a company), head  [here](https://www.investopedia.com/articles/basics/06/invest1000.asp)  for a tutorial.

You’re about to implement C$50 Finance, a web app via which you can manage portfolios of stocks. Not only will this tool allow you to check real stocks’ actual prices and portfolios’ values, it will also let you buy (okay, “buy”) and sell (okay, “sell”) stocks by querying  [IEX](https://iextrading.com/developer/)  for stocks’ prices.

Indeed, IEX lets you download stock quotes via their API (application programming interface) using URLs like  `https://cloud-sse.iexapis.com/stable/stock/nflx/quote?token=API_KEY`. Notice how Netflix’s symbol (NFLX) is embedded in this URL; that’s how IEX knows whose data to return. That link won’t actually return any data because IEX requires you to use an API key (more about that in a bit), but if it did, you’d see a response in JSON (JavaScript Object Notation) format like this:

```
{
  "avgTotalVolume": 4329597,
  "calculationPrice": "tops",
  "change": 1.21,
  "changePercent": 0.00186,
  "closeSource": "official",
  "companyName": "NetFlix Inc",
  "currency": "USD",
  "iexAskPrice": 662.59,
  "iexAskSize": 8080,
  "iexBidPrice": 652.65,
  "iexBidSize": 102,
  "iexClose": 652.66,
  "iexCloseTime": 1636479523133,
  "iexLastUpdated": 1636479523133,
  "iexMarketPercent": 0.03419734093274243,
  "iexOpen": 652.66,
  "iexOpenTime": 1636479523133,
  "iexRealtimePrice": 652.66,
  "iexRealtimeSize": 30,
  "iexVolume": 43968,
  "lastTradeTime": 1636479523133,
  "latestPrice": 652.66,
  "latestSource": "IEX real time price",
  "latestTime": "12:38:43 PM",
  "latestUpdate": 1636479523133,
  "marketCap": 288341929921,
  "openSource": "official",
  "peRatio": 58.85,
  "previousClose": 651.45,
  "previousVolume": 2887523,
  "primaryExchange": "NASDAQ",
  "symbol": "NFLX",
  "week52High": 690.97,
  "week52Low": 463.41,
  "ytdChange": 0.2066202315388457
}
```

**Project Description:**  Platform where users can create an account, , get stocks daya, and buy and sell "fantasy" stocks.

Main building blocks of the projects:

 - `register`: Allows a user to register to platform. The username and
   password are submitted via Flask and stored in a sqlite database.
 - `quote`: Allows a user to look up important data of a stock using the by providing the stock symbol.
 -  `buy`: Allows a user to buy an imaginary stock; purchased stocks are saved to the database and the user balance is updated accordingly.
 -  `sell`: Allows a user to sell his imaginary stocks; sold stocks are removed from the database and the user balance is updated accordingly.
 -   `index`: Displays the user stocks portfolio which is a summary table of the user's current funds and holdings and open positions
 -  `history`: Displays all of the user transaction history

## Configuring

Before getting started on this, we’ll need to register for an API key in order to be able to query IEX’s data. To do so, follow these steps:

-   Visit  [iexcloud.io/cloud-login#/register/](https://iexcloud.io/cloud-login#/register/).
-   Select the “Individual” account type, then enter your name, email address, and a password, and click “Create account”.
-   Once registered, scroll down to “Get started for free” and click “Select Start plan” to choose the free plan.
-   Once you’ve confirmed your account via a confirmation email, visit  [https://iexcloud.io/console/tokens](https://iexcloud.io/console/tokens).
-   Copy the key that appears under the  _Token_  column (it should begin with  `pk_`).
-   In your terminal window, execute:

```
$ export API_KEY=value
```

where  `value`  is that (pasted) value, without any space immediately before or after the  `=`. You also may wish to paste that value in a text document somewhere, in case you need it again later.

## Running

Start Flask’s built-in web server (within  `finance/`):

```
$ flask run
```
