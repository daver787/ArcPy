import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise07"
infc="airports.shp"
outfc="Results/airports_anchorage.shp"
delimitedField=arcpy.AddFieldDelimiters(infc,"COUNTY")
arcpy.Select_analysis(infc,outfc,delimitedField+" = 'Anchorage Borough'")