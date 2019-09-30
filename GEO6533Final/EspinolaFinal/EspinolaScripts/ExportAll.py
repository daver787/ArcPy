#Question 3.3-ExportAll.py:Write a code to export all attributes to a text file for each clipped file,use appropriate ArcMap tool.
#Note in this step some files may be empty(i.e. they will not have any rows in their attribute table),this means you need to test for this,
#and print to the screen if the file you are processing has any rows or not (and the rows count). Find the right ArcMap tool to do this

import arcpy
arcpy.env.workspace="C:/EspinolaFinal/ClippedKEWX"# set the workspace to location of clipped shapefiles
outpath="C:/EspinolaFinal/ExportedKEWX"#folder to output text files
fclist=arcpy.ListFeatureClasses()#create a list of all the clipped feature classes

for fc in fclist:#iterate over the list of feature classes
    rows=arcpy.GetCount_management(fc)[0]#get a count of number of features in attribute table for each feature class
    print("The number of rows in the attribute table of " +fc + " is: "+rows)#print out the number of rows in the attribute table
    if rows>0:# if there are features in the table export the table to a text file in the ExportedKEWX folder
        arcpy.TableToTable_conversion(fc, outpath, str(arcpy.Describe(fc).basename)+".txt")