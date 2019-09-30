# Name: David Espinola
#Date: April 21, 2019
#Description: Challenge 2- You are given a feature class called parcels.shp located in the Exercise12 folder that contains the following fields:
#FID, Shape, Landuse and Value. Modify the parceltax.py script so that it determines the property tax for each parcel and stores these values in a list.append
#You should use the class created in the parcelclass.py script-the class can remain unchanged. Print the values of the final list as follows:
# FID: <property tax>
class Parcel:#define parcel class
    def __init__(self,landuse,value):
        self.landuse=landuse#define attributes of parcel class
        self.value=value#define attributes of parcel class

    def assesment(self):#define assesment function that calculates tax rate based on 3 landuse categories
        if self.landuse=="SFR":
            rate=0.05
        elif self.landuse=="MFR":
            rate=0.04
        else:
            rate=0.02
        assesment =self.value*rate#overall taxes will be the tax rate times the value attribute of class
        return assesment#return overall taxes