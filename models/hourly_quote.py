from orator import Model
from config import db
from orator.orm import belongs_to
import numbers
import datetime

Model.set_connection_resolver(db)

class HourlyQuote(Model):

    __fillable__ = ['datetime', 'price']
    __dates__ = ['datetime']
    __timestamps__ = False

    @belongs_to
    def stock(self):
        return Stock

    @staticmethod
    def is_valid_date(date):
        pass

    @staticmethod
    def is_valid_price(price):
        valid = price and isinstance(price, numbers.Number)
        return True if valid else False

    def is_valid(self):
        return HourlyQuote.is_valid_price(self.price) and \
               HourlyQuote.is_valid_date(self.date)

HourlyQuote.creating(lambda hourly_quote: hourly_quote.is_valid())
