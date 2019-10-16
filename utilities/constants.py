from enum import Enum

class Profiles(Enum):
    ftcr = "config/felipeRibeiro.ini"
    vbbarros = "config/viniciusBarros.ini"

class excptypes(Enum):
    criticalFailure = 0

class Status(Enum):
    initializing = 0
    dbConnFailed = 1

class DbDriverType(Enum):
    postgresql = "postgresql"
    sqlserver = "mssql+pyodbc"
    mysql = "mysql"
    oracle = "oracle"