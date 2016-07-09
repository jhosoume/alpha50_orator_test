from orator import Model
from config import db
from orator.orm import has_many

Model.set_connection_resolver(db)

class Stock(Model):

    @has_many
    def hourly_quotes(self):
        return HourlyQuote

    @has_many
    def daily_quotes(self):
        return DailyQuote

    #@has_many
    #def stocks_portfolios(self):
        #return 
