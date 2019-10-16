#! python2 # -*- coding: utf-8 -*-
# Nome: Utilidades.py
# Data: 2018/12
# Função: Biblioteca de Utilidades utilizadas no mainNebuluz.py
# Autor: Bernardo Viana / Felipe Ribeiro - IHM Stefanini

import logging
from logging import handlers
import GenConfigFile as conf
import os
import sys
import datetime
import signal
from utilEnum import excptypes


##      CONFIGURAÇÃO DE ARQUIVO DE LOG       ##
def configureLog():
    logFile = conf.ReadConfigFile('LOG','filename') #"nebuluzLog.log"
    logging.basicConfig(filename = logFile,
                        level = logging.getLevelName(conf.ReadConfigFile('LOG','level')),
                        format = "%(levelname)s: %(asctime)s %(message)s")

    logging.handlers.RotatingFileHandler(logFile, maxBytes = 1024, backupCount = 1)


##      FUNÇÃO PARA TRATAMENTO DE EXCEÇÕES       ##
def exceptionTreatment(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    strLog = "Critical Failure in file %s line %s :: %s" % (fname, exc_tb.tb_lineno, e)        
    logging.critical(strLog)
    raise        # apagar
    return excptypes.criticalFailure


##      FUNÇÃO PARA TRATAMENTO DE EXCEÇÕES GERAIS       ##
def generalExceptionTreatment(e, message):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    strLog = "%s :: File %s line %s :: %s" % (message, fname, exc_tb.tb_lineno, e)        
    logging.error(strLog) 




