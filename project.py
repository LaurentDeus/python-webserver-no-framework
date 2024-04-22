from flask import Flask, render_template
from cruds import get_all_restaurants, get_restaurant, get_restaurant_menuitems

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def restaurants():
    all_restaurants = get_all_restaurants()
    return render_template('restaurants.htm', restaurants=all_restaurants)


@app.route('/restaurant/<int:restaurant_id>')
def menuitems(restaurant_id):
    restaurant = get_restaurant(id=restaurant_id)
    mi = get_restaurant_menuitems(restaurant_id=restaurant_id)
    data = {'restaurant': restaurant, 'menu_items': mi}
    return render_template('menu_items.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
