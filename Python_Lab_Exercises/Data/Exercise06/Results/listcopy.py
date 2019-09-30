import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise06"
arcpy.CreateFileGDB_management("C:/GEO6533/Python/Data/Exercise06/Results","NM.gdb")
fclist=arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc=arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc,"C:/GEO6533/Python/Data/Exercise06/Results/NM.gdb/"+fcdesc.basename)