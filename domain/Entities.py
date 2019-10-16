from dependencies.base import Base
from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy import Sequence

class Table1(Base):
    __tablename__ = 'Table1'
    
class Table2(Base):
    __tablename__ = 'Table2'




