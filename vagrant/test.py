from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# first = session.query(Restaurant).first()
# print first.name
#
# items = session.query(MenuItem).all()
# for i in items:
#     print i.price
#
# burger = session.query(MenuItem).filter_by(id=1).one()
# burger.price = "$2.99"
# session.add(burger)
# session.commit()

drop = session.query(MenuItem).filter_by(id=9).one()
session.delete(drop)
session.commit()

veggie = session.query(MenuItem).filter_by(name="Veggie Burger")
for veg in veggie:
    print veg.id
    print veg.price
    print veg.restaurant.name
    print "\n"

