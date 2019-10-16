# encoding: utf-8
import configparser
import os.path
from utilities.exceptions import generalExceptionTreatment

class ConfigFile:


    def __init__(self, configName = 'config.ini'):
        self.__configName = configName



    def WriteConfigFile(self):

        if not os.path.isfile(self.__configName):

            config = configparser.ConfigParser()

            config['LOG'] = {}
            config['LOG']['FileName'] = 'kpi-executor.log'
            config['LOG']['Level'] = 'INFO'
            config['LOG']['Format'] = "%(levelname)s: %(asctime)s %(message)s"
            config['LOG']['MaxByte'] = '1024'
            config['LOG']['BackupCount'] = '1'

            config['DATABASE_DASHBOARD'] = {}
            config['DATABASE_DASHBOARD']['IP'] = 'od1rkc5b0lergt8.csydych85aop.us-east-1.rds.amazonaws.com'
            config['DATABASE_DASHBOARD']['Port'] = '5432'
            config['DATABASE_DASHBOARD']['InstanceName'] = 'omo-db'
            config['DATABASE_DASHBOARD']['UserName'] = 'master'
            config['DATABASE_DASHBOARD']['Password'] = 'wjmDEH69WEF6KV4B'
            config['DATABASE_DASHBOARD']['ConnStr'] = "DRIVER={SQL Server};SERVER={serverDB};DATABASE={instancename};UID={username};PWD={password}"
            config['DATABASE_DASHBOARD']['reconnecTimeDelay'] = '20'

            config['DATABASE_KPI'] = {}
            config['DATABASE_KPI']['IP'] = '10.1.8.16'
            config['DATABASE_KPI']['Port'] = '1433'
            config['DATABASE_KPI']['InstanceName'] = 'omokpi'
            config['DATABASE_KPI']['UserName'] = 'master'
            config['DATABASE_KPI']['Password'] = 'wjmDEH69WEF6KV4B'
            config['DATABASE_KPI']['ConnStr'] = "DRIVER={SQL Server};SERVER={serverDB};DATABASE={instancename};UID={username};PWD={password}"
            config['DATABASE_KPI']['reconnecTimeDelay'] = '20'

            with open(self.__configName, 'w') as configfile:
                    config.write(configfile)

    def ReadConfigFile(self, section, option):

        try:        
            config = configparser.ConfigParser()
            config.read(self.__configName)
            return config[section][option]
        except KeyError as e:
            generalExceptionTreatment(e, "Key not found in config file")
            raise e
        except Exception as e:
            generalExceptionTreatment(e,"Failed to read config file")
            raise e
