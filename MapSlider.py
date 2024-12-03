import geopandas as gpd
import pandas as pd
import plotly.express as px

# Read Texas counties shape file
# texas_counties_shp = gpd.read_file(r'C:\Users\The Scholar\Downloads\Project_Relevant\Tx_Census_CntyBndry_Detail_TIGER500k')
texas_counties_shp = gpd.read_file(r'C:\Users\The Scholar\Downloads\Project_Relevant\cleaned_texas_counties.shp')

# Read Texas drought csv file
texas_drought_csv = pd.read_csv(r'C:\Users\The Scholar\Downloads\Project_Relevant\UPDATED CSV DROUGHT.csv')

# Create new column for most severe drought occurrence each week
def most_severe_drought(row):
    # Check the ratings in order from most severe to least severe
    for severity in ["D4", "D3", "D2", "D1", "D0", "None"]:
        if row[severity] > 0:  # If severity is greater than zero then return it
            return severity
    return "None"  # All columns 0, then return "None"

# Use function to create new column in drought csv
texas_drought_csv["Most_Severe_Level"] = texas_drought_csv.apply(most_severe_drought, axis=1)

# Merge the drought data with the shapefile
texas_counties_shp = texas_counties_shp.rename(columns={"NAME": "County"})
merged_data = texas_counties_shp.merge(texas_drought_csv, on="County")

# Change to format used by plotly
geojson_data = merged_data.__geo_interface__

# Create animated choropleth map with a slider for weeks
texas_drought_map = px.choropleth_mapbox(
    merged_data,
    geojson=geojson_data,
    locations="County",
    color="Most_Severe_Level",
    featureidkey="properties.County",
    animation_frame="MapDate",
    mapbox_style="carto-positron", #open-street-map or carto-positron
    center={"lat": 31.9686, "lon": -99.9018},
    zoom=5,
    color_discrete_map={
        "None": "green",
        "D0": "yellow",
        "D1": "orange",
        "D2": "red",
        "D3": "firebrick",
        "D4": "darkred"
    },
    category_orders={
        "Most_Severe_Level": ["D5", "D4", "D3", "D2", "D1", "D0", "None"]
    },
    title= "Texas Drought Levels For 2023"
)

texas_drought_map.update_layout(
    title={
        "text": "Texas Drought Levels For 2023",
        "x": 0.5,  # Center title
        "y": 0.975,  # Lower the title slightly
        "xanchor": "center",
        "yanchor": "top",
        "font": {"size": 22},  # Font size
        "pad": {"t": 10},  # Spacing from top
    },
    legend={
        "title": {"text": "Drought Severity Levels"},
        "yanchor": "bottom",
        "y": 0.027,  # Lower legend
        "xanchor": "left",
        "x": 0.01,  # Move legend left
    },
    margin={"r": 10, "t": 75, "l": 10, "b": 0},
    mapbox={
        "center": {"lat": 31.3, "lon": -99.9}, #31.9686,-99.9008
        "zoom": 4.6,
    },
    updatemenus=[
        {
            "type": "buttons",
            "showactive": False,
            "x": 0.0,  # Move buttons to the left
            "xanchor": "left",
            "y": -0.12,  # Adjust the vertical position
            "yanchor": "middle",
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 1500, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate",
                },
            ],
        }
    ],
    sliders=[
        {
            "x": 0.1, 
            "len": 0.85, 
            "xanchor": "left",
        }
    ],
)

# Show map with slider
texas_drought_map.show()
