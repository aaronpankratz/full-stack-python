from flask import Flask, render_template, url_for

app = Flask(__name__)
#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'id':'1','name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}

@app.route('/')
@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html', restaurants = restaurants)

@app.route('/restaurants/new')
def createRestaurant():
    return render_template('createRestaurant.html')

@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return render_template('editRestaurant.html', restaurant = restaurant)

@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return render_template('deleteRestaurant.html', restaurant = restaurant)
#    return 'page to delete restaurant %s' % restaurant_id

@app.route('/restaurants/<int:restaurant_id>/menu')
def restaurantMenu(restaurant_id):
    return render_template('restaurantMenu.html', restaurant = restaurant, items = items)

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def createItem(restaurant_id):
    return render_template('createItem.html', restaurant = restaurant)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editItem(restaurant_id, menu_id):
    return render_template('editItem.html', restaurant = restaurant, item = item)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteItem(restaurant_id, menu_id):
    return render_template('deleteItem.html', restaurant = restaurant, item = item)

if __name__ == '__main__':
    app.debug = True
    app.run()
