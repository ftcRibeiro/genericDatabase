from searches.Search import * 
from domain.Entities import *

class Table2Search(Search):
    
    def __init__(self, db):
        super().__init__(db)
    

    def setData(self, dataDf):
        return super().setData(dataDf)