import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise06"
if arcpy.Exists("cities.shp"):
    arcpy.CopyFeatures_management("cities.shp","results/cities_copy.shp")
