# Name: David Espinola
#Date: April 21, 2019
#Description: Challenge 1- Create a custom function called countstringfields that determines the number of fileds of type string in an input feature class
#Create this function in a seperate script(for example,mycount.py) that you call from another script(for example,callingscript.py). You can use the streets.shp
# feature class in the Exercise12 folder.
import arcpy
import mycount#import function
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise12"#set workspace

num_strings=mycount.countstringfields("streets.shp")#use function to count number of string fields in streets feature class and save into a variable num_strings
print(num_strings)#print value in num_strings

