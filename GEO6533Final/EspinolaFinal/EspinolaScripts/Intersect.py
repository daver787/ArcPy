#Question 3.2-Intersect.py: Use the projected KEWX shapefiles to intersect (clip) them with the precipitation rain gauges file given to you.
#(output of each clip or intersect should be a point file),again print to the screen the name of the file you are processing and add the suffix(_clip)
# to the output files. Output of this tool should go to the folder "ClippedKEWX".

import arcpy
import os#import os to join paths
data_folder=arcpy.env.workspace="C:/GEO6533Final/Question3/KEWX_Data/KEWX_Data"#path where the rainfall radar data is stored
fclist=arcpy.ListFeatureClasses()#list all the shapefiles in that folder
clipfc="C:\GEO6533Final\Question3\gisFiles\precip_gages_wgs84.shp"# rain gauge shapefile that we are intersecting with all our rainfall radar data
outpath="C:\EspinolaFinal\ClippedKEWX"#folder where all the clipped feature classes are going

for infc in fclist:#iterate through all our projected rainfall radar data shapefiles
    outfc=os.path.join(outpath,arcpy.Describe(infc).basename+"_clip"+".shp")#create the full file name for clipped shapefile,appending "_clip" to the end
    arcpy.Intersect_analysis([infc, clipfc],outfc, output_type="point")#run intersect tool and send the shapefiles to ClippedKEWX folder
    print("Intersect for "+outfc+"_clip"+" completed succesfully.")#print a message once geoprocessing tool has run succesfully