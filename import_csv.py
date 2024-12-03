import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Adjust Pandas settings to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

#Reads the shapefile file in the folder using the path
texas_shp = gpd.read_file(r'C:\Users\Julian\Desktop\gis_programming_folder\Tx_Census_CntyBndry_Detail_TIGER500k')

texas_shp.to_csv('GISProgramming_shapefile_data.csv')
