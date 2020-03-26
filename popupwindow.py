import pandas
import folium

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tile="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

#To add content for the pop up window. +m adds the m for meter to elevation
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location = [lt, ln], popup=str(el)+" m", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map7.html")