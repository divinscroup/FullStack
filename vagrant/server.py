from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def home(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    output = ''
    output += '<h2> %s</h2>' % restaurant.name
    for i in items:
        output += i.name
        output += i.price
        output += '</br>'
        output += i.description
        output += '</br></br>'

    return output


@app.route('/restaurants/<int:restaurant_id>/new/')
def new_menu(restaurant_id):
    return 'page to create a new menu item.'


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def edit_menu(restaurant_id, menu_id):
    return 'page to edit menu item.'


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def del_item(restaurant_id, menu_id):
    return 'page to delete menu item.'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
