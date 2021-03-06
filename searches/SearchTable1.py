from searches.Search import * 
from domain.Entities import *

class Table1Search(Search):

    def __init__(self, db):
        super().__init__(db)

    def getAll(self):
        return super().getAll(Table1)

    def setData(self, dataDf):
        return super().setData(dataDf,Table1)
    
    def getAllTable1ByTable2Id(self, table2Id):
        try:
            q = self.session.query(Table1.name.label('Generic name 1'), Table2.name.label('Generic name 2')) \
                .select_from(Table1) \
                .join(Table2, Table1.table2_id == Table2.id) \
                .filter(Table1.table2_id == table2Id)
            return self.returnQuery(q)

        except Exception as e:
            generalExceptionTreatment(e,"Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))
            raise e

    
