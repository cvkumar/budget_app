from pony.orm import *
from datetime import datetime


def setupDatabase():
    db = Database()

    class Transaction(db.Entity):
        id = PrimaryKey(unicode)
        account_id = Required(unicode)
        name = Required(str)
        amount = Required(float)
        date = Required(datetime)
        default_transaction_type = Optional(str)
        default_category1 = Optional(str)
        default_category2 = Optional(str)
        default_category3 = Optional(str)
        primary_category = Optional(str)
        secondary_category = Optional(str)
        transaction_type = Optional(str)
        owner = Optional(str)

    # db.bind(provider='sqlite', filename=':memory:')
    db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='budget_app')
    set_sql_debug(True)
    db.generate_mapping(create_tables=True)
