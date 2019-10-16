# encoding: utf-8
import configparser
import os.path
from utilities.exceptions import generalExceptionTreatment

class ConfigFile:


    def __init__(self, configName = 'config/config.ini'):
        self.__configName = configName



    def WriteConfigFile(self):

        if not os.path.isfile(self.__configName):

            config = configparser.ConfigParser()

            config['CONFIG_SECTION'] = {}
            config['CONFIG_SECTION']['IP'] = 'xxx.xxx.xxx.xxx'
            config['CONFIG_SECTION']['Port'] = 'xxxx'
            config['CONFIG_SECTION']['InstanceName'] = 'dbName'
            config['CONFIG_SECTION']['UserName'] = 'userName'
            config['CONFIG_SECTION']['Password'] = 'userPassword'
            config['CONFIG_SECTION']['reconnecTimeDelay'] = 'x'

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
