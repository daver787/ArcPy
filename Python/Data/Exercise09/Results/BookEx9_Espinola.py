# Name: David Espinola
#Date: April 2, 2019
#Description: Challenge 1- Create a script that determines what areas meet the following conditions:
#Moderate slope- between 5 and 20 degrees
#Southerly Aspect-between 150 and 270 degrees
#Forested-land-cover types of 41,42,43
import arcpy
from arcpy.sa import *
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise09"#set workspace and import arcpy
arcpy.env.overwriteOutput=True

if arcpy.CheckExtension("spatial")=="Available":#check if spatial analyst is licensed and availabile for use
    arcpy.CheckExtension("spatial")#check out spatial analyst extension
    
    slope=arcpy.Slope("elevation")#create slope raster object from elevation
    aspect=arcpy.Aspect("elevation")#create aspect raster object from elevation
    land_cover=arcpy.Raster("landcover.tif")#create raster object from land cover
    
    good_slope=((slope > 5) & (slope < 20)) #create raster objects with slope between 5 and 20
    good_aspect=((aspect > 150)&(aspect < 270))#create raster object with aspect between 150 and 270
    good_land=((land_cover == 41)|(land_cover == 42)|(land_cover == 43))#create raster object with only land cover types of 41,42 or 43
    good_area=(good_slope & good_aspect & good_land)#combine all these criteria into one raster object 

    good_area.save("challenge1")#save the raster object as "challenge1"
    arcpy.CheckInExtension("spatial")#check back in spatial analyst extension
else:
    print "Spatial Analyst Extension license is not available"

# Name: David Espinola
#Date: April 2, 2019
#Description: Challenge 2- Write a script that copies all rasters in the workspace to a new file geodatabase.
#You can use the rasters in the Exercise09 folder as an example
import os
from arcpy.sa import *
inpath="C:/GEO6533/Python/Data/Exercise09"
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise09"#set workspace and import arcpy
arcpy.env.overwriteOutput=True
arcpy.CreatePersonalGDB_management(path, "pGDB.mdb")#create personal geodatabase
#outpath=os.path.join(inpath,"pGDB.mdb")
outpath="C:/GEO6533/Python/Data/Exercise09/pGDB.mdb"
Rasters=arcpy.ListRasters()#create list of rasters in workspace

for raster in Rasters:#create for loop to iterate over rasters
    raster_name=arcpy.Describe(raster).basename#get name without file extension
     print raster_name#check names are correct
    arcpy.CopyRaster_management(raster,outpath+"/"+raster_name)#copy each raster to personal geodatabase
   

