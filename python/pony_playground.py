from pony.orm import *

if __name__ == "__main__":
    db = Database()


    class Person(db.Entity):
        id = Required()
        name = Required(str)
        age = Required(int)
        cars = Set('Car')


    db.bind(provider='sqlite', filename=':memory:')

