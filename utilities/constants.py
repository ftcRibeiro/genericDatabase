from enum import Enum

class Profiles(Enum):
    dev = "config/developerName.ini"

class excptypes(Enum):
    criticalFailure = 0

class Status(Enum):
    initializing = 0
    dbConnFailed = 1
    dbCreateFailed = 2

class DbDriverType(Enum):
    postgresql = "postgresql"
    sqlserver = "mssql+pyodbc"
    mysql = "mysql"
    oracle = "oracle"