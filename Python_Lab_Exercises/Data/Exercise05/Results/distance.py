import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise05"
if arcpy.CheckExtension("spatial")=="Available":
    arcpy.CheckOutExtension("spatial")
    out_distance=arcpy.sa.EucDistance("bike_routes.shp",cell_size=100)
    out_distance.save("C:/GEO6533/Python/Data/Exercise05/Results/bike_dist")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not availabile"