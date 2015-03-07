from flask import Flask, render_template, url_for, request, redirect, flash
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/menu/items/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    menu_items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html', restaurant = restaurant, items = menu_items)

@app.route('/restaurants/<int:restaurant_id>/menu/items/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name = request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id = restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/menu/items/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    menu_item = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        menu_item.name = request.form['name']
        menu_item.description = request.form['description']
        menu_item.price = request.form['price']
        session.commit()
        flash("menu item updated!")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id = restaurant_id, menu_item = menu_item)

@app.route('/restaurants/<int:restaurant_id>/menu/items/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    menu_item = session.query(MenuItem).filter_by(id = menu_id).one()
    if request.method == 'POST':
        session.delete(menu_item)
        session.commit()
        flash("menu item deleted")
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
    else:
        return render_template('deletemenuitem.html', restaurant_id = restaurant_id, menu_item = menu_item)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run()
