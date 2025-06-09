# Restaurant Geospatial Analysis using Folium

This project visualizes restaurant locations on an interactive map using latitude and longitude data. Developed as part of my Data Science Internship at Cognifyz Technologies, it uses Python libraries Pandas and Folium to create a clear geospatial visualization.

## Project Overview

The goal is to plot restaurant locations from a dataset (`dataset.csv`) on a map, helping to understand their geographic distribution. Each restaurant is shown as a blue dot on the map, with a popup displaying its name.

## Features

- Cleans data by removing entries without valid latitude or longitude.
- Calculates the geographic center of the dataset to center the map.
- Plots restaurants as blue circle markers on an interactive Folium map.
- Saves the final map as `restaurant_map.html` for easy viewing in any browser.

## Files

- `dataset.csv` – Dataset containing restaurant information and coordinates.
- `main.py` – Python script that processes the data and generates the map.
- `restaurant_map.html` – Output interactive map showing restaurant locations.

## Technologies Used

- Python  
- Pandas – for data cleaning and manipulation  
- Folium – for creating interactive maps  

## How to Run

1. Install dependencies:

pip install pandas folium

2. Run the script:

python main.py

3. Open `restaurant_map.html` in your browser to view the map.

## Outcome

An interactive map that visually represents restaurant locations, useful for geospatial analysis, business insights, and planning.
