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

class DatabaseClass:

    def __init__(self, section, conf):

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

    def connectDb(self):
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
            self.__engine = create_engine(conStr)

            Base.prepare(self.__engine, reflect=True)
            self.session = Session(self.__engine)
            return Status.initializing
            
        except Exception as e:
            generalExceptionTreatment(e,"Failed to connect to Database")
            return Status.dbConnFailed
            
    def closeSession(self):
        try:
            self.session.close_all()
        except Exception as e:
            generalExceptionTreatment(e, "Failed to connect to Database")
            raise e
           

   