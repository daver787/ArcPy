import arcpy
mxd="C:/GEO6533/Python/Data/Exercise10/Austin_TX.mxd"
mapdoc=arcpy.mapping.MapDocument(mxd)
dataset="C:/GEO6533/Python/Data/Exercise10/Austin/base.shp"
spatialref=arcpy.Describe(dataset).spatialReference
extent=arcpy.Describe(dataset).extent
for df in arcpy.mapping.ListDataFrames(mapdoc):
    df.spatialReference=spatialref
    df.panToExtent=extent
    df.scale=15000
mapdoc.save()
del mapdoc
