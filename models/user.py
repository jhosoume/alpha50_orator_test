from orator import Model
from config import db

Model.set_connection_resolver(db)

class User(Model):
    pass
