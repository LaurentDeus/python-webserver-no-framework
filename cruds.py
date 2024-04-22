from typing import List, Union
from sqlalchemy.orm import Session
from database import *


def get_restaurant(id: int) -> Union[Restaurant, None]:
    try:
        with Session(engine) as dbsession:
            return dbsession.query(Restaurant).get(id)
    except Exception as e:
        print(f'Error occured while fetching Restaurant with ID {id}', e)


def get_all_restaurants() -> List[Restaurant]:
    with Session(engine) as dbsession:
        restaurants = dbsession.query(Restaurant).all()
    return restaurants


def get_restaurant_names() -> list:
    restaurants = get_all_restaurants()
    return [r.name for r in restaurants]


def create_restaurant(res_name: str) -> bool:
    with Session(engine) as dbsession:
        restaurant = Restaurant(name=res_name)
        try:
            dbsession.add(restaurant)
            dbsession.commit()
            return True
        except Exception as e:
            print('An Error During Restaurant Creation', e)
            return False


def update_restaurant_name(old_id: int, new_name: str) -> bool:
    with Session(engine) as dbsession:
        try:
            old_res = dbsession.query(Restaurant).get(old_id)
            old_res.name = new_name
            dbsession.add(old_res)
            dbsession.commit()
            return True
        except Exception as e:
            print(f'Could not Edit {old_res.name} to {new_name}', e)
            return False


def delete_restaurant(id: int) -> bool:
    with Session(engine) as dbsession:
        try:
            res_to_delete = dbsession.query(Restaurant).get(id)
            dbsession.delete(res_to_delete)
            dbsession.commit()
            return True
        except Exception as e:
            print(f'Could not delete Restaurant with ID {id}', e)
            return False


def get_restaurant_menuitems(restaurant_id: int) -> Union[List[MenuItem], None]:
    with Session(engine) as dbsession:
        try:
            return dbsession.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
        except Exception as e:
            print(
                f'Could not get MenuItems for Restaurant with ID {restaurant_id}', e)
            return

# try two methods, passing ID and passion object


def create_menuitem(restaurant_id: int, name: str, description: str, price: int, course: str) -> bool:
    with Session(engine) as dbsession:
        try:
            restaurant_name = get_restaurant(id=restaurant_id).name
            mi = MenuItem(name=name, restaurant_id=restaurant_id,
                          description=description, price=price, course=course)
            dbsession.add(mi)
            dbsession.commit()
            return True
        except Exception as e:
            print(f'Failed to Add {name} to {restaurant_name} Restaurant', e)
            return


def get_restaurant_menuitem(menuitem_id: int) -> MenuItem:
    with Session(engine) as dbsession:
        try:
            return dbsession.query(MenuItem).get(menuitem_id)
        except Exception as e:
            print(
                f'Could not get MenuItem with ID {menuitem_id}', e)
            return
        
def update_menuitem(menuitem_id: int, name: str, description: str, price: int, course: str) -> bool:
    mi = get_restaurant_menuitem(menuitem_id=menuitem_id)
    mi.name = name
    mi.course = course
    mi.price =  price
    mi.description = description
    with Session(engine) as dbsession:
        try:
            dbsession.add(mi)
            dbsession.commit()
            return True
        except Exception as e:
            print(
                f'Could not update MenuItem with ID {menuitem_id}', e)
            return 
        
def delete_menuitem(menuitem_id:int)->bool:
    with Session(engine) as dbsession:
        try:
            menuitem = dbsession.query(MenuItem).get(menuitem_id)
            dbsession.delete(menuitem)
            dbsession.commit()
            return True
        except Exception as e:
            print(f'Could not delete {menuitem.name}', e)
            return False