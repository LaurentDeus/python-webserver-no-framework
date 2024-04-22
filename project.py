from flask import Flask,render_template
from cruds import get_all_restaurants

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def restaurants():
    all_restaurants = get_all_restaurants()
    return render_template('restaurants.htm',restaurants = all_restaurants)




if __name__ == '__main__':
    app.run(debug=True)