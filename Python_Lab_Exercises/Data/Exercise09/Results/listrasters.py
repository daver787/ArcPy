import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise09"
rasterlist=arcpy.ListRasters()
for raster in rasterlist:
    print raster