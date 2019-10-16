from base import Base
from sqlalchemy import Column
from sqlalchemy import types
from sqlalchemy import Sequence

class Kpi(Base):
    __tablename__ = 'kpi'
    
class BusinessKpi(Base):
    __tablename__ = 'businesskpi'




