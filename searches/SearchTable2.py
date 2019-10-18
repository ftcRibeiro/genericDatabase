from searches.Search import * 
from domain.Entities import *

class Table2Search(Search):
    """ Queries to read and write in Table2 table

    Methods
    -------
        getAll(self)
        setData(self, dataDf)
        getAllByTable1Name(tagName)
            Get all values by table1Name

    """
    def __init__(self, db):
        super().__init__(db)
    
    def getAll(self):
        return super().getAll(Table2)

    def setData(self, dataDf):
        return super().setData(dataDf,Table2)