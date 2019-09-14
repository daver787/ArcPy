# Name: David Espinola
#Date: April 17, 2019
#Description: Challenge 1- The following script contains a number of errors. Try to identify all four.
import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise07"
fc="airports.shp"#should be same case as other uses since python is case sensitive
rows=arcpy.SearchCursor(fc)
fields=arcpy.ListFields(fc)
for field in fields:
    if field.name=="NAME":#missing colon for end of if statement and should be "field" not "fields" since you are accesing individual field object not the whole list
        for row in rows:
            print "Name = {0}".format(row.getValue(field.name))#missing indentation


# Name: David Espinola
#Date: April 17, 2019
#Description: Challenge 2- The following script contains a number of errors. Try to identify all six.
import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise09"#Change the backslash to forward slash 
raster="landcover.tif"#correct file name is "landcover.tif" not "landcover.tiff"
desc=arcpy.Describe(raster)#describe should be capitalized because it is a function
x=desc.meanCellHeight#m should be lowercase but it will still run
y=desc.meanCellWidth# m should be lowercase but it will still run
spatialref=desc.spatialReference#book shows that "s" should be capitalized but Esri site and text of chapter 9 disagree
units=spatialref.linearUnitName
print "Cells are"+str(x)+" by " + str(y)+ " "+ units + "."
