from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

TICKER = [
    "NVDA",
    "AAPL",
    "AMZN",
    "META",
    "TSLA",
    "AMD",
    "GM"
]

@app.route("/")
def index():
    return render_template("index.html", ticker=TICKER)

# https://github.com/ranaroussi/yfinance/tree/main

@app.route("/ticker_details")
def ticker_details():
    selected_ticker = request.args.get('ticker')
    ticker_data = yf.Ticker(selected_ticker)
    ticker_info = ticker_data.info
    ticker_price = ticker_info['currentPrice']
    ticker_name = ticker_info['longName']
    return render_template("ticker_details.html", ticker=selected_ticker, price=ticker_price, name=ticker_name)
