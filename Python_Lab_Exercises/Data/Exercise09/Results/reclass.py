import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace="C:/GEO6533/Python/Data/Exercise09"
if arcpy.CheckExtension("spatial")=="Available":
    arcpy.CheckOutExtension("spatial")
    myremap=RemapRange([[41,1],[42,2],[43,3]])
    outreclass=Reclassify("landcover.tif","VALUE",myremap,"NODATA")
    outreclass.save("lc_recl")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."
