import arcpy
from arcpy import env
env.workspace = "C:/GEO6533/Python/Data/Exercise11"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    desc = arcpy.Describe(fc)
    print desc.basename + ": " + desc.shapeType