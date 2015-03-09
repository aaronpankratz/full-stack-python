from flask import Flask, render_template, url_for, redirect, request
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
        return redirect(url_for('restaurants.html'))

@app.route('/restaurants/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'GET':
        return render_template('editRestaurant.html', restaurant = restaurant)
    else:
        restaurant.name = request.form['name']
        sessiont.commit()
        return redirect(url_for('restaurants.html'))

@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'GET':
        return render_template('deleteRestaurant.html', restaurant = restaurant)
    else:
        session.delete(restaurant)
        sessiont.commit()
        return redirect(url_for('restaurants.html'))

@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return render_template('restaurantMenu.html', restaurant = restaurant, items = items)

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    return render_template('createItem.html', restaurant = restaurant)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return render_template('editItem.html', restaurant = restaurant, item = item)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return render_template('deleteItem.html', restaurant = restaurant, item = item)

if __name__ == '__main__':
    app.debug = True
    app.run()
