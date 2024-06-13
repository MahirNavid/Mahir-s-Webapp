from flask import Flask, render_template, request
import yfinance as yf
from pytickersymbols import PyTickerSymbols

app = Flask(__name__)

stock_data = PyTickerSymbols()
sp100_stocks = list(stock_data.get_stocks_by_index('S&P 100'))
TICKER = []
for stock in sp100_stocks[:30]:
    TICKER.append(stock['symbol'])

PAGE = [1,2,3]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ticker_list")
def ticker_list():
    factor = request.args.get('page', 1, type=int)
    upper = factor*10
    lower = upper-10
    ticker=TICKER[lower:upper]

    ticker_price = []
    ticker_name = []

    for symbol in ticker:
        ticker_data = yf.Ticker(symbol)
        ticker_info = ticker_data.info
        ticker_price.append(ticker_info.get('currentPrice'))
        ticker_name.append(ticker_info.get('longName'))

    return render_template("ticker_list.html", ticker=ticker, page=PAGE, price=ticker_price, name=ticker_name)

# https://github.com/ranaroussi/yfinance/tree/main

@app.route("/ticker_details", methods=["GET"])
def ticker_details():
    selected_ticker = request.args.get('ticker')
    ticker_data = yf.Ticker(selected_ticker)
    ticker_info = ticker_data.info
    ticker_price = ticker_info['currentPrice']
    ticker_name = ticker_info['longName']
    return render_template("ticker_details.html", ticker=selected_ticker, price=ticker_price, name=ticker_name)
