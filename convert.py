import  jpype     
import  asposecells     
import os
jpype.startJVM() 
from asposecells.api import Workbook

routeArchive = "../../../Desktop/rentaAbril2023.xlsx"
nameArchive = os.path.splitext(os.path.basename(routeArchive))[0]
workbook = Workbook(routeArchive)
workbook.save("json/"+nameArchive+".json")
jpype.shutdownJVM()
print("Done!")
