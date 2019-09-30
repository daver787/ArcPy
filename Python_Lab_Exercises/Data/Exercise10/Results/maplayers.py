import arcpy
mxd="C:/GEO6533/Python/Data/Exercise10/Austin_TX.mxd"
mapdoc=arcpy.mapping.MapDocument(mxd)
for df in arcpy.mapping.ListDataFrames(mapdoc):
    print "Data frame "+df.name+ " contians the following layers:"
    lyrlist=arcpy.mapping.ListLayers(mapdoc,"",df)
    for lyr in lyrlist:
        print lyr.name
del mapdoc        