from domain.EntitiesDashboard import *

from Utilidades import *
import inspect
import pandas as pd
import time
class Search():

    def __init__(self, db):
        try:
            self.session = db.session

        except Exception as e:
            raise e


    def returnQuery(self, q, checkNone = False):
        try:
            if q.first() == None and checkNone:            
                logging.info("Following ( {0}) query returns no results :: {1} ".format(inspect.stack()[1][3], q))
                return                
            else:
                return pd.read_sql(q.statement, q.session.bind)

        except Exception as e:
            generalExceptionTreatment(e,"Failed to execute query :: {0} :: SQL = {1}".format(inspect.stack()[1][3], q))
            raise e
            

class SearchDashboard(Search):

    def __init__(self, db):
        super().__init__(db)

    def getAllLoops(self):
        try:
            q = self.session.query(Loop.web_id, Loop.controller_action, Loop.economy_importancy)
            return self.returnQuery(q)

        except Exception as e:
            raise e
            generalExceptionTreatment(e,"Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))

    def getLoopsByClient(self, clientId):
        try:
            q = self.session.query(Loop.name, Client.name.label('client_name')) \
                .select_from(Loop) \
                .join(Client, Loop.client_id == Client.id) \
                .filter(Loop.client_id == clientId)
            return self.returnQuery(q)

        except Exception as e:
            generalExceptionTreatment(e,"Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))
            raise e


class SearchKpi(Search):

    def __init__(self, db):
        super().__init__(db)
    
    def setKpiData(self, **data):
        try:
           pass

        except Exception as e:
            generalExceptionTreatment(e,"Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))
            raise e

    def setBusinessKpiData(self, **data):
        try:
            pass

        except Exception as e:
            raise e