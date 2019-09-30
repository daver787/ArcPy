import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise07"
fc="airports.shp"
unique_name=arcpy.CreateUniqueName("Results/buffer.shp")
arcpy.Buffer_analysis(fc,unique_name,"5000 METERS")
