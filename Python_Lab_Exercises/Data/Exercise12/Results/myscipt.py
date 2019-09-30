import arcpy
import list
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise12"
fields=list.listfieldnames("streets.shp")
print fields