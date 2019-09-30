# Name: David Espinola
#Date: April 8, 2019
#Description: Challenge 1- In ArcGIS for Desktop Help,research the AddLayer function of the ArcPy mapping module and use it
#to write a script that adds the parks layer from the Parks data frome in Austin_TX.mxd to the other two data frames in the same map document

import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise10"
mxd="C:/GEO6533/Python/Data/Exercise10/Austin_TX.mxd"#specify file path for map
mapdoc=arcpy.mapping.MapDocument(mxd)#create map document object
park_df = arcpy.mapping.ListDataFrames(mapdoc,"Parks")[0]#create data frame object for Parks data frame
park_lyr=arcpy.mapping.ListLayers(mapdoc,"parks",park_df)[0]#pass Parks data frame object to ListLayers function to create parks layer object
df = arcpy.mapping.ListDataFrames(mapdoc)#create list of data frames in map document
for dataframe in df:#loop through data frames in math document
    if dataframe.name!="Parks":#add layer to the other data frames besides Parks
        arcpy.mapping.AddLayer(dataframe, park_lyr, "BOTTOM")#use AddLayer function to add parks layer to all data frames besides Parks
mapdoc.saveACopy("C:/GEO6533/Python/Data/Exercise10/Austin_TX1.mxd")#save a copy of map so original is unchanged
del mapdoc,park_lyr,park_df,df#delete map document,layer object and data frame objects to remove any locks on map file
