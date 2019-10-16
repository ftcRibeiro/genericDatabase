from enum import Enum

class Profiles(Enum):
    ftcr = "felipeRibeiro.ini"
    vbbarros = "viniciusBarros.ini"

class excptypes(Enum):
    criticalFailure = 0

class Status(Enum):
    initializing = 0
    dbConnFailed = 1