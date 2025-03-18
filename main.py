import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import folium
from geodatasets import get_path
import geopandas as gpd

# Load the Natural Earth dataset (countries)
world = gpd.read_file("ne_110m_admin_0_countries.shp")
print(world.head())

#Indexing and Selecting Data
# Select a specific country (e.g., Brazil)
brazil = world[world["NAME"] == "Brazil"]
print(brazil)

#Check coordinate reference system with .crs
print(world.crs)
#Reproject to a different CRS (e.g., EPSG 3857 for web mapping)
world = world.to_crs(epsg=3857)
print(world.crs)

#Merging Data
#Load another dataset: Cities
cities = gpd.read_file("ne_110m_populated_places.shp")
cities = cities.to_crs(epsg=3857)
