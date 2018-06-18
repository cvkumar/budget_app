from pony.orm import *
from datetime import datetime

if __name__ == "__main__":
    db = Database()


    class Test(db.Entity):
        id = PrimaryKey(unicode)
        name = Required(str)
        amount = Required(float)


    # db.bind(provider='sqlite', filename=':memory:')
    db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='budget_app')
    set_sql_debug(True)
    db.generate_mapping(create_tables=False)
    # #
    with db_session:
        t = Test(id=unicode(23432), name='John', amount=20)
        commit()
