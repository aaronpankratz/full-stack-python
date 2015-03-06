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
@app.route('/hello')
def hello_world():
    restaurant = session.query(Restaurant).first()
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

if __name__ == '__main__':
    app.debug = True
    app.run()