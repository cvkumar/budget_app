from pony.orm import *
from datetime import datetime
import os

db = Database()


class Transaction(db.Entity):
    id = PrimaryKey(unicode)
    account_id = Required(unicode)
    account_owner = Required(str)
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


def connectDatabase():
    db.bind(provider='postgres', user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('POSTGRES_HOST'), database=os.getenv('DATABASE'))

    set_sql_debug(bool(os.getenv('sql_debug')))
    db.generate_mapping(create_tables=True)
