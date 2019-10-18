from searches.Search import * 
from domain.Entities import *

class ValuesSearch(Search):
    """ Queries to read and write in Values table

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
        return super().getAll(Values)

    def setData(self, dataDf):
        return super().setData(dataDf)
        
    def getAllByTable1Name(self, tagName):
        """ Find values by name
        Parameters
        ----------
            tagName: Tag name from table1

        """

        try:
            q = self.session.query(Values.value.label('Values'), Table1.name.label('Tag'), Values.timestamp.label('Timestamp')) \
                .select_from(Values) \
                .join(Table1, Values.table1_id == Table1.id) \
                .filter(Table1.name == tagName)
            return self.returnQuery(q)

        except Exception as e:
            generalExceptionTreatment(e, "Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))
            raise e