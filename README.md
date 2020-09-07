# Creating-a-Real-Time-Weather-App-with-Flask-Folium-ChartJS-in-Python
This is the complete source code of my article on Medium: <br>
https://medium.com/@litingliaotiff/creating-a-real-time-weather-app-with-flask-folium-chartjs-in-python-495f5533e97f

## What I’m going to make
This is an updated version of my Flask weather app from Taiwan Government Central Weather Bureau 中央氣象局 API, adding folium map and chartJS to it. 

## Environment used in this project
I'm using Python3 in VS code.

## Skills used in this project
* Update the look of the app.
* Roundup the numbers of humidity and temperature from API.
* Add map to mark current locations and nearest weather station using folium.
* Show the latest rainfall forecast, temperature and perceived temperature trend from Taiwan CWB API using chartJS

## Notes for files
* main.py: entry point of flask web app
* templates/weather.html: main layout
* templates/map.html: layout for map
* find_nearest.py: get the nearest weather station's data read depends on your current device's IP location
* pop6h_forecast.py: get the forecast rainfall percentage in the 6 hours from API
* T_AT_forecast.py: get the forecast temperature and perceived temperature in the 3 hours from API

