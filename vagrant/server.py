from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def home():
    return '<h2>Welcome Back !</h2>'
@app.route('/restaurants/<int:restaurant_id>/')
def restaurant_list(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)

    return render_template('menu.html', restaurant=restaurant, items=items)



@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def new_menu(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('restaurant_list', restaurant_id=restaurant_id))
    else:
        return redirect(url_for('newMenu.html', restaurant_id=restaurant_id))



@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def edit_menu(restaurant_id, menu_id):
    return 'page to edit menu item.'


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def del_item(restaurant_id, menu_id):
    return 'page to delete menu item.'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
