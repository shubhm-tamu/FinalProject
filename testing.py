# Social Vulnerability Testing

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Reads the shapefile file in the folder using the path
svi_shp = gpd.read_file(r'C:\Users\Julian\Desktop\gis_programming_folder\CR_ME_SocialVulnerabilityIndex_BG_clip')


#plots the texas shape file
svi_shp.plot(color = 'pink', edgecolor = 'black')

#shows the resulting plot
plt.show()