import arcpy
from arcpy import env
env.workspace="C:GEO6533/Python/Data/Exercise07"
fc="Results/airports.shp"
cursor=arcpy.da.InsertCursor(fc,"NAME")
cursor.insertRow(["New Airport"])
del cursor
                             