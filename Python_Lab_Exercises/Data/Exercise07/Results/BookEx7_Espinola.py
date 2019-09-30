# Name: David Espinola
#Date: March, 1, 2019
#Description: Challenge 1- Write a script that creates a 15,000 meter buffer around features in the airports.shp feature class classified as an airport
#(based on the feature field) and a 7,500-meter buffer around features classified as a seaplane base. The results should be two separate feature classes,one for each airport type.

import arcpy
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise07"#set workspace and import arcpy
infc="airports.shp"#feature class to operate on
delimfield=arcpy.AddFieldDelimiters(infc,"FEATURE")#create delimited field for where clause
arcpy.Select_analysis(infc,"sea_sel.shp",delimfield+"='Seaplane Base'")#create feature class with features from airports with a seaplane base
arcpy.Select_analysis(infc,"air_sel.shp",delimfield+"='Airport'")#create feature class with features from airports with an airport
arcpy.Buffer_analysis("sea_sel.shp","buffer_seaplane.shp","15000 METERS")#create buffer of 15,000 meters around seaplane bases
arcpy.Buffer_analysis("air_sel.shp","buffer_airport.shp","7500 METERS")#create buffer of 7,500 meters around airports



# Name: David Espinola
#Date: March, 1, 2019
#Description: Challenge 2- Write a script that adds a text field to the roads.shp feature class called FERRY and populates this field with YES and NO values,
#depending on the value of the feature field
import arcpy
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise07"#set workspace and import arcpy
fc="roads.shp"#feature class to operate on
newfield="FERRY"#name of new field
fieldtype="TEXT"#type of new field
fieldname=arcpy.ValidateFieldName(newfield)#make sure field name is valid and store in new variable
arcpy.AddField_management(fc,fieldname,fieldtype,"","",12)#add the field to roads feature class
cursor=arcpy.da.UpdateCursor(fc,["FEATURE","FERRY"])#create cursor to iterate through the rows of attribute to update new FERRy field
for row in cursor:
    if row[0]=="Ferry Crossing":#if the feature is a ferry crossing fill the FERRY field with "YES"
        row[1]="YES"
    else:
        row[1]="NO"#if feature is another type fill ferry field with "NO"
    cursor.updateRow(row)#update the row
del row
del cursor#delete cursor and row to remove lock on file
                    