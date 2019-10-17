from searches.Search import * 
from domain.Entities import *

class ValuesSearch(Search):

    def getAllByTable1Name(self, tagName):
        try:
            q = self.session.query(Values.value.label('Values'), Table1.name.label('Tag'), Values.timestamp.label('Timestamp')) \
                .select_from(Values) \
                .join(Table1, Values.table1_id == Table1.id) \
                .filter(Table1.name == tagName)
            return self.returnQuery(q)

        except Exception as e:
            generalExceptionTreatment(e, "Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))
            raise e

    def setItem(self, dataDf):
        try:
            __timestamp = int(time.time())

            for i in range(0, len(dataDf)):  # apagar - remover a /2
                NAME = dataDf.at[i, 'name']                
                TABLE2_ID = str(dataDf.at[i, 'table2_id'])
                                
                q = Table1( insert_date=__timestamp,
                                name=NAME, table2_id=TABLE2_ID)
                
                self.session.add(q)
                self.session.commit()
            
        except Exception as e:
            generalExceptionTreatment(e, "Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))