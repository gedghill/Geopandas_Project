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
world = world.to_crs(epsg=4326)
print(world.crs)

#Merging Data
#Load another dataset: Cities
cities = gpd.read_file("ne_110m_populated_places.shp")
#Reproject cities to match world dataset
cities = cities.to_crs(epsg=4326)
#Spatial join: find cities within each country
cities_with_country = gpd.sjoin(cities,world, how='inner', predicate='within')
print(cities_with_country.head())

#Plot the world map with cities
fig, ax = plt.subplots(figsize=(10, 10))
world.plot(ax=ax, color='lightgray')
cities.plot(ax=ax, marker='o', color='red', markersize=5)
ctx.add_basemap(ax, crs=world.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)
plt.title('World Countries and Cities')
plt.show()

#Create an interactive map
m = folium.Map(location=[0,0],zoom_start=2)
#Add cities to the map
for idx, row in cities.iterrows():
    folium.Marker(
        location=[row.geometry.y,row.geometry.x],
        popup=row['NAME']
    ).add_to(m)

#Save the map to an HTML file
m.save('world_cities_map.html')