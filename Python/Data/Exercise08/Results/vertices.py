import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise08"
fc="rivers.shp"
cursor=arcpy.da.SearchCursor(fc,["OID@","SHAPE@"])
for row in cursor:
    print("Feature {0}: ".format(row[0]))
    for point in row[1].getPart(0):#used to get first part of first and only part of the geometry since this isnt multipart polygon
        print("{0},{1}".format(point.X,point.Y))