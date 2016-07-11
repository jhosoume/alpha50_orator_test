from yahoo_finance import Share
import sys
import arrow
from decimal import Decimal
from models.stock import Stock
from models.daily_quote import DailyQuote


BEG = '2016-06-01'
END = '2016-06-30'

def get_stock_history(ticker, beg, end):
    history = Share(ticker).get_historical(beg, end)
    prep_history = []
    for day in history:
        info = {'date': arrow.get(*[ int(num) for num in day['Date'].split('-') ]), 
                'close_price': Decimal(day['Close'])}
        prep_history.append(info)
    return prep_history
    
        #if not stock.daily_quotes().save_many( [ DailyQuote(day)  for day in get_stock_history(stock.ticker, BEG, END) ] )
def populate_stock_history(beg, end):
    for stock in Stock.all():
        for day in get_stock_history(stock.ticker, BEG, END):
            if not stock.daily_quotes().save(DailyQuote(day)):
                print("ERROR: could not save daily quote for \n {}".format(day))
    

