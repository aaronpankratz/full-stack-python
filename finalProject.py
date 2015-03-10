from flask import Flask, render_template, url_for, redirect, request, jsonify
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurants = session.query(Restaurant).all();
    return render_template('restaurants.html', restaurants = restaurants)

@app.route('/restaurants/new', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'GET':
        return render_template('createRestaurant.html')
    else:
        restaurant = Restaurant(name = request.form['name'])
        session.add(restaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))

@app.route('/restaurants/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'GET':
        return render_template('editRestaurant.html', restaurant = restaurant)
    else:
        restaurant.name = request.form['name']
        session.commit()
        return redirect(url_for('showRestaurants'))

@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'GET':
        return render_template('deleteRestaurant.html', restaurant = restaurant)
    else:
        session.delete(restaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))

@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    menuItems = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return render_template('restaurantMenu.html', restaurant = restaurant, items = menuItems)

@app.route('/restaurants/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'GET':
        return render_template('createMenuItem.html', restaurant = restaurant)
    else:
        menuItem = MenuItem(restaurant_id = restaurant_id, name = request.form['name'], description = request.form['description'], price = request.form['price'])
        session.add(menuItem)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    menuItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'GET':
        return render_template('editMenuItem.html', restaurant = restaurant, item = menuItem)
    else:
        menuItem.name = request.form['name']
        menuItem.description = request.form['description']
        menuItem.price = request.form['price']
        session.commit()
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    menuItem = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'GET':
        return render_template('deleteMenuItem.html', restaurant = restaurant, item = menuItem)
    else:
        session.delete(menuItem)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id = restaurant_id))

@app.route('/restaurants/JSON')
def restaurantJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[restaurant.serialize for restaurant in restaurants])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def menuJSON(restaurant_id):
    menu = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return jsonify(MenuItems=[item.serialize for item in menu])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id = menu_id).one()
    return jsonify(MenuItem=menuItem.serialize)

if __name__ == '__main__':
    app.debug = True
    app.run()
