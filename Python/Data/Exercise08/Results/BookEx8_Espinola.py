# Name: David Espinola
#Date: March, 8, 2019
#Description: Challenge 1- Write a script that creates a new polygon feature class containing a single (square) polygon with the following coordinates:
#(0,0) ,(0,1000),(1000,0) and (1000, 1000)
import arcpy
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise08"#set workspace and import arcpy
arcpy.env.overwriteOutput=True
poly_coords=[(0,0,0),(1,0,1000),(2,1000,1000),(3,1000,0)]#coordiantes of rectangle with id as first value
outpath="C:/GEO6533/Python/Data/Exercise08"
newfc="Results/challenge_1_poly.shp"
arcpy.CreateFeatureclass_management(outpath,newfc,"Polygon")#create the challenge_1_poly.shp feature class
cursor=arcpy.da.InsertCursor(newfc,["SHAPE@"])#initiate a search cursor to insert the geometry into feature class
array=arcpy.Array()#create array to hold coordinates of polygon
point=arcpy.Point()#create point object to create point geometry for polygon
for coords in poly_coords:#iterate over tuples in poly_coords list
    ID,X,Y=coords#pull out individual values
    point.ID=ID#assign id to id attribute of point class
    point.X=X#assign X to X attribute of point class
    point.Y=Y#assign Y to Y attribute of point class
    array.add(point)#add the point to array
cursor.insertRow([arcpy.Polygon(array)])#create polygon object from point and insert into geometry field of feature class
del cursor#remove lock on feature class
    



# Name: David Espinola
#Date: March, 8, 2019
#Description: Challenge 2- Write a script that determines the perimeter (in meters) and area(in square meters) of each of the individual islands of the Hawaii.shp
#feature class. Recall that this is a multipart feature class
import arcpy
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise08"set workspace and import arcpy
fc="Hawaii.shp"
cursor=arcpy.da.SearchCursor(fc,["OID@","SHAPE@"])#initiate a search cursor for the Hawaii.shp feature class
for row in cursor:#iterate through the rows of feature class
    print("Feature {0}: ".format(row[0]))#print out id value of feature
    partnum=0#create counter to keep track of which part of hawaii we are getting the values for
    for part in row[1]:#iterate through the parts of multipart feature class Hawaii.shp
        print("Part {0}: ".format(partnum))#print out part number of feature
        geom=arcpy.Geometry("polygon",part)#create a geometry object for each part
        print("The perimeter of part number "+str(partnum)+ " is : "+str(geom.getLength("PLANAR","METERS")))#access the perimeter method of geometry object and print value to screen 
        print("The area of part number "+str(partnum)+ " is : "+str(geom.getArea("PLANAR","SQUAREMETERS")))#access the area method of geometry object and print value to screen
        partnum=partnum+1#add one to part counter
del cursor# remove lock on Hawaii feature class


# Name: David Espinola
#Date: March, 8, 2019
#Description: Challenge 3- Write a script that creates an envelope feature class for the Hawaii.shp feature class
#There is actually a tool that accomplishes this called Minimum Bounding Geometry. You can look at the tool to get
#some ideas,but your script needs to work directly with the geometry properties. 
import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise08"
fc="Hawaii.shp"#feature class we are bounding
new_fc="rectangle.shp"#name of bounding feature class
list_x=[]#create a list to hold x coordinates of Hawaii points
list_y=[]#create a list to hold y coordinates of Hawaii points
coord_array=arcpy.Array()#create array that will hold coordinates of bounding polygon
cursor=arcpy.da.SearchCursor(fc,["OID@","SHAPE@"])#initiate search cursor to access data in Hawaii feature class
for row in cursor:#iterate throght the rows of feature class Hawaii.shp
    for part in row[1]:#iterate through the parts of the multipart feature class Hawaii.shp
        for point in part:#iterate through the points for each part of Hawaii.shp
            list_x.append(point.X)#append x values of point to list_x
            list_y.append(point.Y)#append y values of point to list_y
del cursor#remove lock on Hawaii.shp feature class

#four corners of rectangle
max_x=max(list_x)
min_x=min(list_x)
max_y=max(list_y)
min_y=min(list_y)
coord_list=[[min_x,min_y],[min_x,max_y],[max_x,max_y],[max_x,min_y]]#create list of sublists that contain the corners of the rectangle

arcpy.CreateFeatureclass_management("C:/GEO6533/Python/Data/Exercise08/Results",new_fc,"Polygon")#create new feature class for bounding rectangle
cursor1=arcpy.da.InsertCursor("C:/GEO6533/Python/Data/Exercise08/Results/rectangle.shp",["SHAPE@"])#initiate new insert cursor for rectangle.shp feature class    
point2=arcpy.Point()#create point object to hold points of rectangle
num=0#initiate counter variable to use for point ids
for coord in coord_list:#loop through sub list in coord_list
    point2.ID=num#assign id number to point
    point2.X=coord[0]#assign first element of sub list to x coordinate
    point2.Y=coord[1]#assign second element of sub list to y coordinate
    coord_array.add(point2)#add the point to coord_array
    num=num+1   #increment the id counter variable by 1 
polygon=arcpy.Polygon(coord_array)#create polygon objecrt from points in array
cursor1.insertRow([polygon])#insert  geometry of polygon into first feature in feature class
del cursor1#remove the lock on rectangle.shp feature class

                             