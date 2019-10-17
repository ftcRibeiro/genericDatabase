#! python3 # -*- coding: utf-8 -*-

import inspect
import pandas as pd
import time
from utilities.exceptions import *

# Nome: Search.py
# Data: 2019/10
# Função: Classe genérica de pesquisa baseada na ORM sqlalchemy.
# Autor: Felipe Ribeiro - IHM Stefanini

class Search():

    def __init__(self, db):
        try:
            self.session = db.session

        except Exception as e:
            raise e

#Método para tradução de objeto de retorno de pesquisa para objeto pandas

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

    def setData(self, dataDf):
        """ Write the data set :dataDf: in a table
        Parameters
        ----------
            dataDf: dataframe pandas with all data to insert in a table. This dataframe must have the same table column names

        """
        try:
            __timestamp = int(time.time())
            dataDict = dataDf.to_dict('index')
            q = []
            
            for i in range(1,len(dataDict)):
                q[i] = self(dataDict[i])
            self.add_all(q)
            self.commit()
            self.flush()

        except Exception as e:
            generalExceptionTreatment(e, "Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))