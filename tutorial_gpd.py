import geopandas as gpd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/jcanalesluna/bcn-geodata/master/districtes/districtes.geojson'

districts = gpd.read_file(url)

districts.plot()

plt.show()