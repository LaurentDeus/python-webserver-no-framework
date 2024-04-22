from flask import Flask, redirect, render_template, request, url_for
from cruds import create_menuitem, get_all_restaurants, get_restaurant, get_restaurant_menuitems

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


@app.route('/restaurant/<int:restaurant_id>/<int:menuitem_id>/edit')
def edit_menuitem(restaurant_id: int, menuitem_id: int):
    return render_template('edit_menuitem.html', rid=restaurant_id, mid=menuitem_id)


@app.route('/restaurant/<int:restaurant_id>/<int:menuitem_id>/delete')
def delete_menuitem(restaurant_id, menuitem_id):
    return render_template('delete_menuitem.html', rid=restaurant_id, mid=menuitem_id)


@app.route('/restaurants/<int:restaurant_id>/new_menuitem', methods=['post', 'get'])
def add_new_menuitem(restaurant_id):
    if request.method == 'GET':
        return render_template('add_new_menuitem.html', rid=restaurant_id)
    menuitem_name = request.form.get('menuitem_name')
    description = request.form.get('description')
    price = request.form.get('price')
    course = request.form.get('course')

    if create_menuitem(restaurant_id, menuitem_name, description, price, course):
        return redirect(url_for('menuitems', restaurant_id=restaurant_id))
    return render_template('add_new_menuitem.html', rid=restaurant_id)


if __name__ == '__main__':
    app.run(debug=True)
