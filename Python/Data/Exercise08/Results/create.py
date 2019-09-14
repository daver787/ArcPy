import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise08"
env.overwriteOutput=True
outpath="C:/GEO6533/Python/Data/Exercise08"
newfc="Results/newpolyline.shp"
arcpy.CreateFeatureclass_management(outpath,newfc,"Polyline")
infile="C:GEO6533/Python/Data/Exercise08/coordinates.txt"
cursor=arcpy.da.InsertCursor(newfc,["SHAPE@"])
array=arcpy.Array()
