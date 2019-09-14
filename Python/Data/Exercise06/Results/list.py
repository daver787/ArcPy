import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise06"
fclist=arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe=arcpy.Describe(fc)
    print "Name: "+fcdescribe.name
    print "Data type: "+fcdescribe.dataType