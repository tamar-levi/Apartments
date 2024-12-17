from sqlalchemy import Column, Integer, String, Float, Text, Enum
from ..app import db

class Apartment(db.model):
    __tablename__ = 'apartments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    neighborhood = Column(String(100), nullable=False)
    street = Column(String(100), nullable=False)
    num_build = Column(Integer, nullable=False)
    num_apartment = Column(Integer, nullable=False)
    num_rooms = Column(Integer, nullable=False)
    floor = Column(Integer, nullable=False)
    apartmentType = Column(Enum('HousingUnit', 'Apartment', 'Duplex', 'Cottage', 'Warehouse'), nullable=False)
    meters = Column(Float, nullable=False)
    air_directions = Column(String(100), nullable=False)
    porch = Column(String(100), nullable=False)
    elevator = Column(String(100), nullable=False)
    yard = Column(String(100), nullable=False)
    furniture = Column(String(100), nullable=False)
    solar_heaters = Column(String(100), nullable=False)
    sukkah = Column(String(100), nullable=False)
    air_conditioner = Column(String(100), nullable=False)
    enter_date = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    flexible_price = Column(Float, nullable=False)
    description = Column(Text, nullable=False)
    start_hour = Column(String(100), nullable=False)
    end_hour = Column(String(100), nullable=False)
    takanon = Column(String(100), nullable=False)
    user_mail = Column(String(100), nullable=False,)
