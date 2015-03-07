from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants')
def restaurants():
    return 'page to display all restaurants'

@app.route('/restaurants/new')
def createRestaurant():
    return 'page to create a restaurant'

@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return 'page to edit restaurant %s' % restaurant_id

@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return 'page to delete restaurant %s' % restaurant_id

@app.route('/restaurants/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
    return 'page to display restaurant %s\'s menu' % restaurant_id

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def createMenuItem(restaurant_id):
    return 'page to create a new menu item for restaurant %s' % restaurant_id

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return 'page to edit menu item %s for restaurant %s' % (menu_id, restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    return 'page to delete menu item %s for restaurant %s' % (menu_id, restaurant_id)

if __name__ == '__main__':
    app.debug = True
    app.run()
