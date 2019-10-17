#! python3 # -*- coding: utf-8 -*-
# Nome: DatabaseClass.py
# Data: 2019/10
# Função: Classe genérica para conexão a banco de dados.
# Autor: Felipe Ribeiro - IHM Stefanini

from sqlalchemy.orm import Session, aliased, Load, load_only
from sqlalchemy import create_engine, func, union, distinct
import pandas as pd
import urllib
from dependencies.base import Base
import logging
import datetime
import inspect
import time
from utilities.GenConfigFile import ConfigFile
from utilities.exceptions import generalExceptionTreatment
from utilities.constants import *
from sqlalchemy.ext.declarative import declarative_base
class DatabaseClass:
    """ Generic class for instantiating a python database, regardless of database provider
    Methods 
    -------
        connectDb(newDatabase = False)
            Connect to a database according to the configuration file used.

    """
    
    def __init__(self, section, conf):

        """
        Parameters
        ----------
            section: section of .ini configuration archive
            conf: name of .ini configuration archive

        """

        try:
            self.__conf = conf
            self.__ip = self.__conf.ReadConfigFile(section,'ip')
            self.__port = self.__conf.ReadConfigFile(section,'port')
            self.__instancename = self.__conf.ReadConfigFile(section,'instancename')
            self.__username = self.__conf.ReadConfigFile(section,'username')
            self.__password = self.__conf.ReadConfigFile(section,'password')
            self.__driver = self.__conf.ReadConfigFile(section,'driver')
                 
                            
        except Exception as e:
            generalExceptionTreatment(e,"Failed to create Database object")

    def connectDb(self,newDatabase = False):

        """ Connect to a database according to the configuration file used. 
        Parameters
        ----------
            newDatabase == false -> Existing Database Reflection
            newDatabase == true -> Creating schema according Base derivated class on project 

        """
        try:
            if(self.__driver == DbDriverType.postgresql.name):
                self.driver = DbDriverType.postgresql.value

            elif(self.__driver == DbDriverType.mysql.name):
                self.driver = DbDriverType.mysql.value

            elif(self.__driver == DbDriverType.oracle.name):
                self.driver = DbDriverType.oracle.value

            elif(self.__driver == DbDriverType.sqlserver.name):
                self.driver = DbDriverType.sqlserver.value

            conStr = "%s://%s:%s@%s/%s" %(self.driver, self.__username, self.__password, self.__ip, self.__instancename)

            if newDatabase:
                Base = declarative_base()
                self.__engine = create_engine(conStr)
                Base.metadata.create_all(self.__engine)
            else:
                self.__engine = create_engine(conStr)
                Base.prepare(self.__engine, reflect=True)
            
            self.session = Session(self.__engine)
            return Status.initializing
            
        except Exception as e:
            generalExceptionTreatment(e,"Failed to connect to Database")
            return Status.dbConnFailed
            
    
    def closeSession(self):
        """ Discconect and cloese session of that database instance
  
        """

        try:
            self.session.close_all()
        except Exception as e:
            generalExceptionTreatment(e, "Failed to connect to Database")
            raise e
           

   