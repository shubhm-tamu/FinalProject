import geopandas as gpd
import pandas as pd

# Step 1: Define file paths
csv_path = r'E:\Documents\LabsFieldGeo\texas_counties_svi_scores.csv'
shapefile_path = r'E:\Documents\LabsFieldGeo\Tx_Census_CntyBndry_Detail_TIGER500k.shp'

# Read the shapefile into a GeoDataFrame
texas_counties_shp = gpd.read_file(shapefile_path)

# Read the CSV into a DataFrame
texas_svi_data = pd.read_csv(csv_path)

# Step 2: Clean the 'COUNTY' columns by stripping whitespaces and converting to uppercase for uniformity
texas_counties_shp['COUNTY'] = texas_counties_shp['COUNTY'].str.strip().str.upper()
texas_svi_data['COUNTY'] = texas_svi_data['COUNTY'].str.strip().str.upper()

# Remove 'COUNTY' from the CSV 'COUNTY' column
texas_svi_data['COUNTY'] = texas_svi_data['COUNTY'].str.replace(r'\sCOUNTY$', '', regex=True)

# Step 3: Inspect unique counties from both datasets for discrepancies
print("Unique counties in shapefile:", texas_counties_shp['COUNTY'].unique()[:10])  # Display first 10
print("Unique counties in CSV:", texas_svi_data['COUNTY'].unique()[:10])  # Display first 10

# Step 4: Merge the shapefile with the CSV on 'COUNTY'
joined_data = texas_counties_shp.merge(texas_svi_data, on='COUNTY', how='inner')

# Check if the merge has produced any rows
if joined_data.empty:
    print("Warning: No matching counties found between shapefile and CSV.")
else:
    # Step 5: Save the merged data as a shapefile and CSV
    output_shapefile = r'E:\Documents\LabsFieldGeo\overall_shapefile_for_walker.shp'
    output_csv = r'E:\Documents\LabsFieldGeo\output_joined_for_walker.csv'

    joined_data.to_file(output_shapefile)
    joined_data.drop(columns='geometry').to_csv(output_csv, index=False)  # Drop 'geometry' for CSV output

    print("Merged data saved:")
    print(f" - Shapefile: {output_shapefile}")
    print(f" - CSV: {output_csv}")

# Print the first few rows of the merged data for verification
print(joined_data.head())