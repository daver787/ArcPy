#Question 3.1-DefineProjection.py-to define the coordiante system of all KEWX shapefiles,use WGS 1984. Make sure that for each file when the
#Define Projection tool is run succesfully you print that to the screen along with the file name just processed.

import arcpy
data_folder=arcpy.env.workspace="C:/GEO6533Final/Question3/KEWX_Data/KEWX_Data"#path where the rainfall radar data is stored
fclist=arcpy.ListFeatureClasses()#list all the shapefiles in that folder
sr = arcpy.SpatialReference("WGS 1984")#create a spatial reference object with the coordinate system WGS 1984 to pass the the Define Projection tool
for fc in fclist:#iterate over the shapefiles
    arcpy.DefineProjection_management(fc,sr)#project each shapefile to coordinate system WGS 1984
    print("Coordinate system is: "+arcpy.Describe(fc).spatialReference.name)#print name of coordinate system to make sure tool ran correctly
    print(fc+" proceesed succesfully")#print another confirmation message that the tool ran succesfully