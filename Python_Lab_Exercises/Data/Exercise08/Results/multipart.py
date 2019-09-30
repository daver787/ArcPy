import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise08"
fc="Hawaii.shp"
cursor=arcpy.da.SearchCursor(fc,["OID@","SHAPE@"])
for row in cursor:
    print("Feature {0}: ".format(row[0]))
    partnum=0
    for part in row[1]:
        print("Part {0}: ".format(partnum))
        for point in part:
            print("{0},{1}".format(point.X,point.Y))
        partnum=partnum+1    
        