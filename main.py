
import pandas as pd
import folium

df=pd.read_csv("Dataset .csv")

df_geospatial=df.dropna(subset=['Latitude','Longitude'])

map_center=[df_geospatial['Latitude'].mean(),df_geospatial['Longitude'].mean()]

restaurant_map=folium.Map(location=map_center,zoon_start=12)
for _, row in df_geospatial.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'],row['Longitude']],
        radius=2,
        popup=row['Restaurant Name'],
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(restaurant_map)
restaurant_map.save("restaurant_map.html")
print("File Created!")
