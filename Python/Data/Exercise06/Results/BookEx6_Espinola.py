# Name: David Espinola
#Date: February, 22, 2019
#Description: Challenge 1- Write a script that reads all feature classes in a workspace and prints the name and geometry type of that feature class in the following format
#streams is a point feature class

import arcpy
path=arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise06"#set workspace and import arcpy

fclist=arcpy.ListFeatureClasses()#List all feature classes in the workspace

for fc in fclist:
    fcdesc=arcpy.Describe(fc)#creates describe object
    print (fcdesc.basename+ " is a "+fcdesc.shapeType+ " feature class")#loop through feature classes and print name and geometry type



# Name: David Espinola
#Date: February, 22, 2019
#Description: Challenge 2- Write a script that reads all feature classes in a personal or file geodatbase and copies only the polygon feature classes to a new file geodatabase.
#You can assume there are no feature datasets in the existing data, and the feature classes can keep the same name.

import arcpy
path="C:/GEO6533/Python/Data/Exercise06/Results/NM.gdb"#variable to store workspace path
arcpy.env.workspace=path#set workspace and import arcpy
gdbname="Test.gdb"#variable to store name of geodatabase being created
fclist=arcpy.ListFeatureClasses("","POLYGON","")#List all polygon feature classes
arcpy.CreateFileGDB_management("C:/GEO6533/Python/Data/Exercise06/Results",gdbname)#creates new file geodatabase
for fc in fclist:
    arcpy.CopyFeatures_management(fc,"C:/GEO6533/Python/Data/Exercise06/Results/"+gdbname+"/"+fc)#loops throgh polygon feature classes and copies them to new geodatabase
    