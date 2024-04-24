from flask import Flask, flash, redirect, render_template, request, url_for
from cruds import create_menuitem, get_all_restaurants, get_restaurant, get_restaurant_menuitem, get_restaurant_menuitems, update_menuitem,delete_menuitem as deleteMenuitem

app = Flask(__name__)
app.secret_key = 'mysecretkey'


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


@app.route('/restaurant/<int:restaurant_id>/<int:menuitem_id>/edit', methods=['post', 'get'])
def edit_menuitem(restaurant_id: int, menuitem_id: int):
    if request.method == 'POST':
        menuitem_name = request.form.get('menuitem_name')
        description = request.form.get('description')
        price = request.form.get('price')
        course = request.form.get('course')
        if update_menuitem(menuitem_id,menuitem_name,description,price,course):
            return redirect(url_for('menuitems', restaurant_id=restaurant_id))
        return render_template('edit_menuitem.html', **request.form)
    menuitem_data = {}
    menuitem_data['restaurant'] = get_restaurant(id=restaurant_id)
    menuitem_data['menuitem'] = get_restaurant_menuitem(menuitem_id)
    return render_template('edit_menuitem.html', **menuitem_data)


@app.route('/restaurant/<int:restaurant_id>/<int:menuitem_id>/delete',methods=['post','get'])
def delete_menuitem(restaurant_id, menuitem_id):
    if request.method == 'POST':
        if deleteMenuitem(menuitem_id):
            return redirect(url_for('menuitems', restaurant_id=restaurant_id))
    menuitem_data = {}
    menuitem_data['restaurant'] = get_restaurant(id=restaurant_id)
    menuitem_data['menuitem'] = get_restaurant_menuitem(menuitem_id)
    return render_template('delete_menuitem.html', **menuitem_data)


@app.route('/restaurants/<int:restaurant_id>/new_menuitem', methods=['post', 'get'])
def add_new_menuitem(restaurant_id):
    if request.method == 'GET':
        return render_template('add_new_menuitem.html', rid=restaurant_id)
    menuitem_name = request.form.get('menuitem_name')
    description = request.form.get('description')
    price = request.form.get('price')
    course = request.form.get('course')

    if create_menuitem(restaurant_id, menuitem_name, description, price, course):
        flash(f'{menuitem_name} Menuitem Created Successfully!')
        return redirect(url_for('menuitems', restaurant_id=restaurant_id))
    return render_template('add_new_menuitem.html', rid=restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/menu/json')
def menuitems_api(restaurant_id):
    menuitems = get_restaurant_menuitems(restaurant_id)
    return [mi.serialize for mi in menuitems] #because menuitems are not json serializable


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menuitem_id>/json')
def menuitem_api(restaurant_id,menuitem_id):
    mi = get_restaurant_menuitem(menuitem_id,restaurant_id=restaurant_id)
    if mi:
        return mi.serialize
    return "Json Respose With Error"

if __name__ == '__main__':
    app.run(debug=True)
