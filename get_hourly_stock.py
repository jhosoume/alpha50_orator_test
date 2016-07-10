import requests
import json
from stocks_list import stocks
from models.stock import Stock 
from models.hourly_quote import HourlyQuote

yahoo_url = 'http://finance.yahoo.com/webservice/v1/symbols/{}/quote?format=json&view=detail'

stocks_info = requests.get(yahoo_url.format(','.join([ str(ticker) for ticker in stocks ])))
stocks_list = json.loads(stocks_info.text)['list']['resources']
stocks_list = [ stock['resource'] for stock in stocks_list ]
