# Name: David Espinola
#Date: April 21, 2019
#Description: Challenge 2- You are given a feature class called parcels.shp located in the Exercise12 folder that contains the following fields:
#FID, Shape, Landuse and Value. Modify the parceltax.py script so that it determines the property tax for each parcel and stores these values in a list.append
#You should use the class created in the parcelclass.py script-the class can remain unchanged. Print the values of the final list as follows:
# FID: <property tax>
import arcpy
import parcelclass#import the parcel class so it can be called used in this script
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise12"#set workspace
fc="parcels.shp"#set feature class to be used 
list=[]#initialize an empty list
cursor=arcpy.da.SearchCursor(fc,["FID","Landuse","Value"])#create a search cursor to access fields in parcels feature class

for row in cursor:    #iterate through rows of feature class using cursor object
    myparcel=parcelclass.Parcel(row[1],row[2])#instantiate a parcel object and pass to it Landuse and Value parameters
    mytax=myparcel.assesment()#call the assesmnet method of the myparcel object to calculate tax for the parcel
    list.append(mytax)#append tax for parcel to list
    print "FID{0}: ".format(row[0])+str(mytax)#print the FID and taxes for each feature in feature class