import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise06"
fieldlist=arcpy.ListFields("cities.shp")
for field in fieldlist:
    print field.name+" "+field.type
    