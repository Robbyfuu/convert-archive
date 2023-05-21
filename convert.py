    
import os
from asposecells.api import Workbook

def convert_excel_to_json(file_path):
    try:
        name_archive = os.path.splitext(os.path.basename(file_path))[0]
        workbook = Workbook(file_path)
        workbook.save("json/" + name_archive + ".json")
        print("Done!")
        return True
    except Exception as e:
        print("Error al convertir archivo: " + str(e))
        return False
