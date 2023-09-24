from flask import Flask, request, jsonify
import yfinance as yf
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is the server for the ticker viewer application.'

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    ticker = request.json['ticker']

    stock = yf.Ticker(ticker)
    data = stock.history(period="2y")
    data.reset_index(inplace=True)

    stock_data = data.to_dict(orient='records')

    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(debug=True)
