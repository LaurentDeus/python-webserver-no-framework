from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine


class Base(DeclarativeBase):
    pass


class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name: Mapped[str]
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    price: Mapped[int]
    course: Mapped[str]
    restaurant_id: Mapped[int] = mapped_column(ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'menu_name': self.name,
            'description': self.description,
            'price': self.price,
            'course': self.course
        }


engine = create_engine('sqlite:///restaurant.db', echo=True)
Base.metadata.create_all(engine)


# print(dir(engine))
# print()
# print()
# print(dir(engine.connect()))
