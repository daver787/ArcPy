import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise07"
fc="Results/airports.shp"
newfield="NEW CODE"
fieldtype="TEXT"
fieldname=arcpy.ValidateFieldName(newfield)
fieldlist=arcpy.ListFields(fc)
fieldnames=[]
for field in fieldlist:
    fieldnames.append(field.name)
if fieldname not in fieldnames:
    arcpy.AddField_management(fc,fieldname,fieldtype,"","",12)
    print("New field has been added.")
 else:
    print("Field name already exists")
