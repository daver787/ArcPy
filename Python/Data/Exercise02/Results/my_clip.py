import arcpy
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise02"
arcpy.Clip_analysis("lakes.shp","basin.shp","Results/lakes_myClip.shp")