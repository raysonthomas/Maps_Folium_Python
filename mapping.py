import folium

map = folium.Map(location=[80, -100])
print(map)
map.save("map1.html")

map = folium.Map(location=[38.58, -99.09], zoom_start=6)
print(map)
map.save("map2.html")

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tile="Stamen Terrain")
print(map)
map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.save("map3.html")

#Feature Group
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map4.html")

#Multiple Points
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tile="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
for coordinates in [[38.2, -99.1],[39.2, -97.1]]:
    fg.add_child(folium.Marker(location= coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("Map5.html")

#Points from Files




