import arcpy
from arcpy import env
env.workspace="C:/GEO6533/Python/Data/Exercise09"
raster="tm.img/Layer_1"
desc=arcpy.Describe(raster)
x=desc.meanCellHeight
y=desc.meanCellWidth
spatialref=desc.spatialReference
units=spatialref.angularUnitName
print "The raster resolution of Band 1 is "+str(x)+ " by "+str(y)+" "+units+"."
