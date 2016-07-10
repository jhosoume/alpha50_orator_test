import json
import requests
from stocks_list import stocks

res = requests.get('http://data.okfn.org/data/core/s-and-p-500-companies/r/constituents-financials.json')
stocks_info = json.loads(res.text)
stocks_info = list(filter(lambda stock: stock['Symbol'] in stocks, stocks_info))
