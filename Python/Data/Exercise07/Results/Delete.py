import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise07"
fc="Results/airports.shp"
cursor=arcpy.da.UpdateCursor(fc,["TOT_ENP"])
for row in cursor:
    if row[0]<100000:
        cursor.deleteRow()
del row
del cursor