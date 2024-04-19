from typing import Union
from sqlalchemy.orm import Session
from database import *


def get_restaurant(id:int)->Union[Restaurant,None]:
    try:
        with Session(engine) as dbsession:
           return dbsession.query(Restaurant).get(id)
    except Exception as e:
        print(f'Error occured while fetching Restaurant with ID {id}',e)

def get_all_restaurants() -> Restaurant:
    with Session(engine) as dbsession:
        restaurants = dbsession.query(Restaurant).all()
    return restaurants


def get_restaurant_names() -> list:
    restaurants = get_all_restaurants()
    return [r.name for r in restaurants]


restaurants_names = get_restaurant_names()

def create_restaurant(res_name:str)->bool:
    with Session(engine) as dbsession:
        restaurant = Restaurant(name = res_name)        
        try:
            dbsession.add(restaurant)
            dbsession.commit()
            return True
        except Exception as e:
            print('An Error During Restaurant Creation',e)
            return False



