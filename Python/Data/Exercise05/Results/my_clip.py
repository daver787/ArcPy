import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise05"
env.overwriteOutput=True
newclip=arcpy.Clip_analysis("bike_routes.shp","parks.shp","Results/bike_Clip.shp")
fCount=arcpy.GetCount_management("Results/bike_Clip.shp")
msgCount=newclip.messageCount
print newclip.getMessage(msgCount-1)