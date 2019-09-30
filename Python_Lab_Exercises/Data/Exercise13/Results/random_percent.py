# Name: David Espinola
#Date: May 1, 2019
#Description: Challenge 1- Make a copy of the random_sample.py script and call it random_percent.py. Modify the script so that the third parameter
#is a percentage of the number of input records between 1 and 100.Modify the script tool settings so that the input for this parameter is validated on the tool dialog box.

import arcpy
import numpy as np# import numpy instead of random to use the random function without replacement from it
from arcpy import env
env.overwriteoutput = True
inputfc = arcpy.GetParameterAsText(0)# Get the input feature class from the user
outputfc = arcpy.GetParameterAsText(1)#get the output feature class from the user
outpercent = int(arcpy.GetParameterAsText(2))#get the percentage from the user and convert it to an integer
desc = arcpy.Describe(inputfc)#create a describe object to access properties of input feature class
inlist = []#create a list in which you will put the OIDs of the features
randomlist = []#create a list to fill with OIDs of random features chosen.
fldname = desc.OIDFieldName#access the OID field name of input feature class
rows = arcpy.SearchCursor(inputfc)#create a search cursor to iterate over the rows of input feature class
row = rows.next()#a variable that will be true as long as it is not at the last row of feature class
while row:#iterate over feature class until the last feature
    id = row.getValue(fldname)#get OIDs
    inlist.append(id)#add OID to list
    row = rows.next()#go to next row if possible   
while len(randomlist) < int((outpercent/float(100))*len(inlist)):#converts percentage given as user input into decimal and multiplies it by number of features in input feature class,which is length of inlist, to give you number of random features to select
    selitem = np.random.choice(inlist,replace=False)#picks random features from OID list without replacement
    randomlist.append(selitem)#appends random feature to randomlist
    #inlist.remove(selitem) not needed since we are using numpy function instead that picks random numbers without replacement
length = len(str(randomlist))
delimfield=arcpy.AddFieldDelimiters(inputfc,fldname)#use this to make sure SQL expression has correct delimiters
sqlexp = delimfield + " in " + "(" + str(randomlist)[1:length - 1] + ")"# create SQL expression to select all the OIDS in randomlist
arcpy.MakeFeatureLayer_management(inputfc, "selection",sqlexp)# create a feature layer from selected OIDS
arcpy.CopyFeatures_management("selection", outputfc)#copy that feature layer into an output feature class specified in the dialog box
