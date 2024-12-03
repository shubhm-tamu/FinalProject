import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Reads the shapefile file in the folder using the path
texas_pop_shp = gpd.read_file(r'C:\Users\Julian\Desktop\gis_programming_folder\Tx_Census_CntyBndry_Detail_TIGER500k')
texas_hhsize_shp = gpd.read_file(r'C:\Users\Julian\Desktop\gis_programming_folder\Tx_Census_CntyBndry_Detail_TIGER500k')

#shows the resulting plot
fig, (ax1, ax2) = plt.subplots(ncols= 2)
texas_pop_shp.plot(ax = ax1, cmap = 'turbo', edgecolor = 'black', column = 'POP_2010')
texas_hhsize_shp.plot(ax = ax2, cmap = 'turbo', edgecolor = 'black', column = 'AVG_HHSIZE')

plt.title(label = "Sample Text",
          loc="left",
          fontstyle='italic')

plt.show()