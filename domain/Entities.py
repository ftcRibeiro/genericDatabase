from dependencies.base import Base
from sqlalchemy.types import *
from sqlalchemy import Table, Sequence, Column, ForeignKey
from sqlalchemy.orm import relationship

seq = Sequence(name='baseSequence', increment=1, minvalue=1)
class Table2(Base):
    __tablename__ = 'Table2'
    id = Column(BigInteger, Sequence('seq') ,primary_key=True)
    name = Column(String, name ='name')
    tb1 = relationship('Table1',backref = 'Table2')
class Table1(Base):
    __tablename__ = 'Table1'
    id = Column(BigInteger, Sequence('seq'), primary_key=True)
    name = Column(String, name='name')
    table2_id = Column(BigInteger,ForeignKey(Table2.id))
    val = relationship('Values',backref = 'Table1')
    
class Values(Base):
    __tablename__ = 'Values'
    id = Column(BigInteger, Sequence('seq'), primary_key=True)
    table1_id = Column(BigInteger,ForeignKey(Table1.id))
    timestamp = Column(TIMESTAMP)


