import sys
from utilities.constants import *
from utilities.DatabaseClass import *
from utilities.exceptions import *
from utilities.GenConfigFile import ConfigFile
# from searches.SearchTable1 import *
from searches import SearchTable1
from searches import SerchValues

parameters = sys.argv[1:]
profile = parameters[0]
conf = ConfigFile(Profiles[profile].value)
table2Id = 1

try:
    db = DatabaseClass('CONFIG_SECTION',conf)

except Exception as eDb:
    exceptionTreatment(eDb)

try:
    if (isinstance(db, DatabaseClass)):
        
        kpiExec = db.connectDb()
        repo = SearchTable1.Table1Search(db)
        data = repo.getAllTable1ByTable2Id(table2Id)

        repo2 = SerchValues.ValuesSearch(db)
        print(data)

        db.closeSession()

except Exception as e:
    exceptionTreatment(e) 