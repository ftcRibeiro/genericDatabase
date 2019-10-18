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
    """ Base class to represent relational database queries
 


        Methods
        -------
            getAll(self, table)
                Get all values by table
            setData(self, dataDf, table)
                Set a dataframe data into a database table
            returnQuery(self, q, checkNone=False)
                Query Return Transformation for Pandas Object 

    """
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

    def getAll(self, table):
        """ Get all values by table
        Parameters
        ----------
            table: name of entity representing table to query
        """
        try:
            q = self.session.query(table)
            return self.returnQuery(q)

        except Exception as e:
            raise e
            generalExceptionTreatment(e,"Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))

    def setData(self, dataDf, table):
        """ Set a dataframe data into a database table
        Parameters
        ----------
            dataDf: dataframe pandas with all data to insert in a table. This dataframe must have the same table column names
            table: name of entity representing table to be changed
        """
        try:
            __timestamp = int(time.time())
            dataDict = dataDf.to_dict('index')
            n = len(dataDict)
            q = [0]*n
            
            for i in range(0,n):
                q[i] = table(**dataDict[i])
            self.session.add_all(q)
            self.session.commit()
            self.session.flush()

        except Exception as e:
            generalExceptionTreatment(e, "Couldn't initiate the query :: {0}".format(inspect.stack()[0][3]))