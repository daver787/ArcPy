# Name: David Espinola
#Date: February, 19, 2019
#Description: Challenge 1-Answer questions about Dissolve and Add XY Coordinates tools


#Question 1: What are the required paramenters for the Add XY Coordinates tool?
# The required parameters are the in_features or feature layer that you want to add the xy cooordinates.

#Question 2: What are the optional parameters for the Add XY Coordiantes tool, and what are their defaults?
#The Add XY Coordiantes tool has no optional parameters.

#Question 1: What are the required paramenters for the Dissolve tool?
#The required parameters are th in_features or features to be aggregated and the out_feature_class i.e. the name of the feature class to be created once aggregation is done.

#Question 2: What are the optional parameters for the Dissolve tool, and what are their defaults?
#The optional parameters for the Dissolve tool are the dissolve_field,statisitcs_field,multi_part and unsplit_lines.
#The dissolve field and statistics_field parameters have no default. Multi_part has a default of "MULTI_PART" and unsplit_lines has a default of "DISSOLVE_LINES".

# Name: David Espinola
#Date: February, 15, 2109
#Description: Challenge 2-Run Add XY Features tool on hospitals.shp feature class

import arcpy
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise05"#set workspace

arcpy.AddXY_management("hospitals.shp")# add XY coordinates to hospitals.shp points feature class


# Name: David Espinola
#Date: February, 15, 2109
#Description: Challenge 3-Run Dissolve tool on the parks.shp feature class using PARK_TYPE as aggregating field. Specify no multipart features are allowed.

import arcpy
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise05"#set workspace
arcpy.Dissolve_management("parks.shp","dissolved_park.shp",["PARK_TYPE"],"","SINGLE_PART","")#dissolve parks.shp based on park type and create single part feature

# Name: David Espinola
#Date: February, 15, 2109
#Description: Challenge 4-Write a script to determine if the following extensions are availabile:"ArcGIS 3D Analyst, ArcGIS Network Analyst, and ArcGIS Spatial Analyst.
#The script should print an informative message with the results such as "The following extensions are available..."

import arcpy
ext_list=["3D","Network","Spatial"] # create list with extension codes of selected extensions
present=[]# create an empty list that will hold extensions that are present

for ext in ext_list: # create loop to loop over extensions in list
    if arcpy.CheckExtension(ext)=="Available":   #check if exrtension is availabile
        present.append("ArcGIS "+ext+" Analyst") # append the full name of the extension if it is availabile

print ("The following extensions are available: "+str(present)) #print the list of availabile extensions
    








