import numbers

def is_valid_ticker(ticker):
    return ticker and ticker.isupper()

def is_valid_sector(sector):
    return sector and (sector in ['Consumer Discretionary', 
                                  'Consumer Staples', 
                                  'Energy',
                                  'Financials',
                                  'Health Care',
                                  'Industrials',
                                  'Information Technology',
                                  'Telecommunications Services'])

def is_valid_market_cap(market_cap):
    return market_cap and isinstance(market_cap, numbers.Number)

def is_valid_stock(stock):
    return stock and \
           is_valid_ticker(stock['ticker']) and \
           is_valid_sector(stock['sector']) and \
           is_valid_market_cap(stock['market_cap'])

