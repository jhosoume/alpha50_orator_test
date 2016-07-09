from orator import Model
from config import db
from orator.orm import belongs_to

Model.set_connection_resolver(db)

class HourlyQuote(Model):

    @belongs_to
    def stock(self):
        return Stock
