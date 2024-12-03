import geopandas as gpd

# Load the original shapefile
texas_counties_shp = gpd.read_file(r'C:\Users\The Scholar\Downloads\Project_Relevant\Tx_Census_CntyBndry_Detail_TIGER500k')

# Remove unnecessary columns
columns_to_keep = ['NAME', 'geometry']
texas_counties_shp = texas_counties_shp[columns_to_keep]

# Simplify the geometry (optional)
texas_counties_shp['geometry'] = texas_counties_shp['geometry'].simplify(tolerance=0.01)  # Adjust tolerance as needed

# Save the cleaned shapefile
cleaned_shapefile_path = r'C:\Users\The Scholar\Downloads\Project_Relevant\cleaned_texas_counties.shp'
texas_counties_shp.to_file(cleaned_shapefile_path)

print("Cleaned shapefile saved at:", cleaned_shapefile_path)