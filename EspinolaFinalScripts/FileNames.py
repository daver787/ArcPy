#Question 1.2-FileNames.py: Write a python script that creates text file with all the file names in each folder(2008 and 2009).
#You can either use ArcGIS raster listing function or just python listing function.
import arcpy
import os
workspace="C:\GEO6533Final"
rasters = []
f=open("C:/EspinolaFinal/rasternames.txt","w")
walk = arcpy.da.Walk(workspace, topdown=True, datatype="RasterDataset")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        rasters.append(filename)
        f.write(str(filename)+"\n")
f.close()        