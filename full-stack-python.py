from flask import Flask
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/menu/items')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    menu_items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ''
    for menuItem in menu_items:
        output += menuItem.name
        output += ' '
        output += menuItem.price
        output += '</br>'
        output += menuItem.description
        output += '</br></br>'
    return output

@app.route('/restaurants/<int:restaurant_id>/menu/items/new')
def newMenutItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

@app.route('/restaurants/<int:restaurant_id>/menu/items/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

@app.route('/restaurants/<int:restaurant_id>/menu/items/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"

if __name__ == '__main__':
    app.debug = True
    app.run()