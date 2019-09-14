# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# soil.py
# Created on: 2019-05-12 13:36:36.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
soils = "soils"
basin = "basin"
soils_Clip1_shp = "C:\\GEO6533\\Python\\Data\\Exercise02\\Results\\soils_Clip1.shp"
soils_Clip1_Select_shp = "C:\\GEO6533\\Python\\Data\\Exercise02\\Results\\soils_Clip1_Select.shp"

# Process: Clip
arcpy.Clip_analysis(soils, basin, soils_Clip1_shp, "")

# Process: Select
arcpy.Select_analysis(soils_Clip1_shp, soils_Clip1_Select_shp, "\"FARMLNDCL\" ='Not prime farmland'")

