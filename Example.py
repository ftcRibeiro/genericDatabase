import sys
from utilities.constants import *
from utilities.DatabaseClass import *
from utilities.exceptions import *
from utilities.GenConfigFile import ConfigFile
# from searches.SearchTable1 import *
from searches import SearchTable2
from searches import SerchValues

parameters = sys.argv[1:]
profile = parameters[0]
conf = ConfigFile(Profiles[profile].value)
table2Id = 1
instData = pd.DataFrame({'name': ['Bernardo', 'Felipe', 'Fred', 'Gustavo', 'Vinicius'] })

try:
    db = DatabaseClass('CONFIG_SECTION',conf)

except Exception as eDb:
    exceptionTreatment(eDb)

try:
    if (isinstance(db, DatabaseClass)):
        
        kpiExec = db.connectDb(newDatabase=True)
        repo = SearchTable2.Table2Search(db)

        repo2 = SerchValues.ValuesSearch(db)
        repo.setData(instData)

        print(instData)

        db.closeSession()

    

except Exception as e:  
    exceptionTreatment(e) 