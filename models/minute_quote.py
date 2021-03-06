from orator import Model
from config import db
from orator.orm import belongs_to, scope
import numbers
import arrow

Model.set_connection_resolver(db)

class MinuteQuote(Model):

    __fillable__ = ['datetime', 'price']
    __dates__ = ['datetime']
    __timestamps__ = False

    @belongs_to
    def stock(self):
        return Stock

    @staticmethod
    def is_valid_datetime(datetime):
        valid = datetime and isinstance(datetime, arrow.Arrow) and \
            datetime > arrow.get('2008-12-31', 'YYYY-MM-DD').to('PST') and \
            datetime < arrow.now().replace(minutes = +5)
        return True if valid else False

    @staticmethod
    def is_valid_price(price):
        valid = price and isinstance(price, numbers.Number)
        return True if valid else False

    @scope
    def older(self, query):
        return query.where('datetime', '<', arrow.now().to('PST').replace(days = +5))

    def is_valid(self):
        return MinuteQuote.is_valid_price(self.price) and \
               MinuteQuote.is_valid_datetime(self.datetime)

    def is_new_range(self):
        count = MinuteQuote.where_between('datetime', [arrow.now().to('PST').replace(minutes = -30), arrow.now().to('PST').replace(minutes = +30)]).count() 
        return True if (count > 0) else False

    def has_record(self):
        count = MinuteQuote.where('stock_id', self.stock_id).where('datetime', self.datetime.datetime).count()
        return True if (count > 0) else False

MinuteQuote.saving(lambda hourly_quote: hourly_quote.is_valid() and not hourly_quote.has_record())
