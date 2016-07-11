import requests
import json
from decimal import Decimal
import arrow
from stocks_list import stocks
from models.stock import Stock 
from models.hourly_quote import HourlyQuote

YAHOO_URL = 'http://finance.yahoo.com/webservice/v1/symbols/{}/quote?format=json&view=detail'


def get_stocks_real_time(tickers_list):
    stocks_info = requests.get(YAHOO_URL.format(','.join([ str(ticker) for ticker in tickers_list ])))
    stocks_list = json.loads(stocks_info.text)['list']['resources']
    stocks_prices = []
    for stock in stocks_list:
        stock = stock['resource']['fields']
        info = {'datetime': arrow.get(stock['utctime']).to('PST'),
                'price': Decimal(stock['price']) } 
        stocks_prices.append({'ticker': stock['symbol'], 'info': info})
    return stocks_prices

def populate_stock_real_time():
    stocks_prices = get_stocks_real_time([stock.ticker for stock in Stock.all()])
    for stock_price in stocks_prices:
        stock = Stock.where('ticker', stock_price['ticker']).first()
        if stock:
            import pdb; pdb.set_trace()
            stock.hourly_quotes().save(HourlyQuote(stock_price['info']))


