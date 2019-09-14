# Name: David Espinola
#Date: April 21, 2019
#Description: Challenge 1- Create a custom function called countstringfields that determines the number of fileds of type string in an input feature class
#Create this function in a seperate script(for example,mycount.py) that you call from another script(for example,callingscript.py). You can use the streets.shp
# feature class in the Exercise12 folder.
import arcpy
arcpy.env.workspace="C:/GEO6533/Python/Data/Exercise12"
def countstringfields(fc):#function header with one required parameter of feature class for function that counts number of string fields in feature class
    count=0#initialize counter variable to zero 
    fields=arcpy.ListFields(fc)#create list of field objects
    for field in fields:#iterate over list of field objects
        if field.type=="String":#check attribute of field object to find if it is of string data type
            count=count+1# if field is string add one to counter variable
    return count#return count 
if __name__=='__main__':#test function if it is run by itself
    countstringfields("streets.shp")

    