from flask import Flask

app = Flask(__name__)


@app.route('/')
def restaurants():
    return "List Of Restaurants"




if __name__ == '__main__':
    app.run(debug=True)