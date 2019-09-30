import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise07"
fc="airports.shp"
delimitedField=arcpy.AddFieldDelimiters(fc,"COUNTY")
cursor=arcpy.da.SearchCursor(fc,["NAME"],delimitedField+" = 'Anchorage Borough'")
for row in cursor:
    print row[0]
del row
del cursor