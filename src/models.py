import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)

class Planet(Base):

    __tablename__ = 'planet'
    uid = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    created = Column(Date, nullable=False)
    edited = Column(Date, nullable=False)
    name = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

class Character(Base):

    __tablename__ = 'character'
    uid = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    created = Column(Date, nullable=False)
    edited = Column(Date, nullable=False)
    name = Column(String(250), nullable=False)
    homeworld = Column(Integer, ForeignKey('planet.uid'), nullable=False)
    planet = relationship(Planet)

    def to_dict(self):
        return {}

class Favorites_planets(Base):

    __tablename__ = 'favorites_planets'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship(User)
    planet_uid = Column(Integer, ForeignKey('planet.uid'), primary_key=True)
    planet = relationship(Planet)

    def to_dict(self):
        return {}
    
class Favorites_characters(Base):

    __tablename__ = 'favorites_characters'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship(User)
    character_uid = Column(Integer, ForeignKey('character.uid'), primary_key=True)
    character = relationship(Character)
    
    def to_dict(self):
        return {}
    
# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')