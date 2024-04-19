from sqlalchemy.orm import Session
from database import *

def get_all_restaurants()->Restaurant:
    with Session(engine) as dbsession:
        restaurants = dbsession.query(Restaurant).all()        
    return restaurants

def get_restaurant_names()->list:
    restaurants = get_all_restaurants()
    return [r.name for r in restaurants]