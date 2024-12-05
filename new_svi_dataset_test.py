#New SVI Index
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
svi_data = pd.read_csv("C:\\Users\\Julian\\Desktop\\gis_programming_folder\\svi_filtered.csv")

# Inspect the dataset
print(svi_data.head())

# Normalize selected variables
variables = [
    'E_POV150', 'E_UNEMP', 'E_HBURD', # Socioeconomic
    'E_AGE65', 'E_AGE17', 'E_DISABL', 'E_SNGPNT', # Household composition
    'E_MINRTY', # Minority and Language
    'E_MUNIT', 'E_MOBILE', 'E_CROWD', 'E_NOVEH' # Housing/Transportation
]

# Normalize each variable
for var in variables:
    svi_data[var + "_pctile"] = svi_data[var].rank(pct=True)

# Compute SVI
svi_data['socioeconomic_svi'] = svi_data[['E_POV150_pctile', 'E_UNEMP_pctile', 'E_HBURD_pctile']].mean(axis=1)
svi_data['household_svi'] = svi_data[['E_AGE65_pctile', 'E_AGE17_pctile', 'E_DISABL_pctile', 'E_SNGPNT_pctile']].mean(axis=1)
svi_data['minority_language_svi'] = svi_data[['E_MINRTY_pctile']].mean(axis=1)
svi_data['housing_transport_svi'] = svi_data[['E_MUNIT_pctile', 'E_MOBILE_pctile', 'E_CROWD_pctile', 'E_NOVEH_pctile']].mean(axis=1)

# Compute overall SVI
svi_data['overall_svi'] = svi_data[['socioeconomic_svi', 'household_svi', 'minority_language_svi', 'housing_transport_svi']].mean(axis=1)

# Save results
svi_data[['NAME', 'overall_svi']].to_csv("texas_counties_svi_scores.csv", index=False)

print("SVI scores calculated and saved to 'texas_counties_svi_scores.csv'")
