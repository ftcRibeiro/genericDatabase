#! python3 # -*- coding: utf-8 -*-
# Nome: DatabaseClass.py
# Data: 2018/12
# Função: Classe genérica para conexão a banco de dados.
# Autor: Felipe Ribeiro - IHM Stefanini

from sqlalchemy.orm import Session, aliased, Load, load_only
from sqlalchemy import create_engine, func, union, distinct
import pandas as pd
import urllib
# import Tables as t
import base
from GenConfigFile import ConfigFile
import logging
import datetime
import inspect
import time
from Utilidades import generalExceptionTreatment
from utilEnum import *


##     BANCO DE DADOS     ##
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
            self.__connstr = self.__conf.ReadConfigFile(section,'connstr')
                 
                            
        except Exception as e:
            generalExceptionTreatment(e,"Failed to create Database object")

    def connectDb(self):
        try:
            if(self.__driver == 'PostgreSQL'):
                conStr = "postgresql://%s:%s@%s/%s" %(self.__username, self.__password, self.__ip, self.__instancename)

            elif(self.__driver == 'MySQL'):
                conStr = "mysql://%s:%s@%s/%s" %(self.__username, self.__password, self.__ip, self.__instancename)

            elif(self.__driver == 'Oracle'):
                conStr = "oracle://%s:%s@%s/%s" %(self.__username, self.__password, self.__ip, self.__instancename)

            elif(self.__driver == 'SQL Server'):
                conStr = "mssql+pyodbc://%s:%s@%s/%s" %(self.__username, self.__password, self.__ip, self.__instancename)
                
            self.__engine = create_engine(conStr)

            base.Base.prepare(self.__engine, reflect=True)
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
           

   