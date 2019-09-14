import arcpy
import os
from arcpy import env
try:
    env.workspace = "C:/GEO6533/Python/Data/Exercise11"
    fclist = arcpy.ListFeatureClasses()
    for fc in fclist:
        desc = arcpy.Describe(fc)
        arcpy.CopyFeatures_management(fc, os.path.join("Results/mydata.mdb", desc.basename))
except arcpy.ExecuteError:
    print arcpy.GetMessages(2)
except:
    print "There has been a nontool error"
    