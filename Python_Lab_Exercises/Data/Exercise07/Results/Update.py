import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise07"
fc="Results/airports.shp"
delimfield=arcpy.AddFieldDelimiters(fc,"STATE")
cursor=arcpy.da.UpdateCursor(fc,["STATE"],delimfield+" <> 'AK' ")
for row in cursor:
    row[0]="AK"
    cursor.updateRow(row)
del row
del cursor