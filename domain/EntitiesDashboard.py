from base import Base
from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy import Sequence

class Loop(Base):
    __tablename__ = 'loop'
    
class Client(Base):
    __tablename__ = 'client'

class Location(Base):
    __tablename__ = 'location'



