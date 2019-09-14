#Question 1.3-RasterClip.py:Write a second script to "subset"(or clip) each grid file to the coterminous US,
#and name the new files like this:
#                               "usa_2008001" for the first one and
#                               "usa_2008002" for the second one and so on

import arcpy
import os#to be used to join path and filename together in script
arcpy.CheckOutExtension("Spatial")
workspace=arcpy.env.workspace="C:/GEO6533Final/Question1"#set the workspace
clipfc="C:/GEO6533Final/Question1/gis_files/usa.shp"#coterminous US feature class to clip the rasters
walk=arcpy.da.Walk(workspace,topdown=True,datatype="RasterDataset")#function that walks through the folders in a directory and gives you acccess
#to filenames,directory names and file paths. Also a filter that brings back only the raster datasets is applied

for dirpath,dirnames,filenames in walk:#loop through all the raster dataset in the workspace
        for filename in filenames:
                if "2008" in str(filename):#if the raster is from 2008 send it to the clipped_ims_2008 folder
                        output_raster=arcpy.sa.ExtractByMask(os.path.join(dirpath, filename),clipfc)#do an extract by mask to clip raster to coterminous united states
                        output_raster.save("C:/EspinolaFinal/clipped_ims_2008/" + "usa_"+str(filename)[1:])#append the "usa_" to the name and remove the "g" by starting at 2nd character of string by using index of 1 in string slice
                elif "2009" in str(filename):#if the raster is from 2009 send it to the clipped_ims_2009 folder
                        output_raster=arcpy.sa.ExtractByMask(os.path.join(dirpath, filename),clipfc)#do an extract by mask to clip raster to coterminous united states
                        output_raster.save("C:/EspinolaFinal/clipped_ims_2009/" + "usa_"+str(filename)[1:])#append the "usa_" to the name and remove the "g" by starting at 2nd character of string by using index of 1 in string slice
                        
arcpy.CheckInExtension("Spatial")        
                
            
 