import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise07"
fc="airports.shp"
cursor=arcpy.da.SearchCursor(fc,["NAME"])
for row in cursor:
    print"Airport name={0}".format(row[0])