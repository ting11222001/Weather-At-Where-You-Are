# Libraries for flask web libraries
# pip3 install flask
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)
app.config['DEBUG'] = True

# dashboard's data calulcation from these files
import find_nearest
import pop6h_forecast
import T_AT_forecast

@app.route('/', methods = ['get'])
def home():
    weather, my_lat, my_lon = find_nearest.find_nearest()
    return render_template('weather.html', weather = weather, my_lat = my_lat, my_lon = my_lon)

@app.route('/data_pop6h_forecast', methods = ['get'])
def data_pop6h_forecast():
    data_pop6h_time_dic = pop6h_forecast.pop6h_forecast()
    return jsonify(data_pop6h_time_dic)

@app.route('/data_T_AT_forecast', methods = ['get'])
def data_T_AT_forecast():
    data_AT_time_dic, data_T_time_dic = T_AT_forecast.T_AT_forecast()
    return jsonify(data_AT_time_dic, data_T_time_dic)

import folium
@app.route('/map', methods = ['get'])
def show_map():
    weather, my_lat, my_lon = find_nearest.find_nearest()
    #create map object
    # show entire Taiwan: 23.6978° N, 120.9605° E
    m = folium.Map([23.6978, 120.9605], zoom_start=8)
    # create markers
    # current location: Latitude: 25.0143, Longitude: 121.4672
    # replace this with (my_lat, my_lon) from find_nearest.py
    folium.Marker([my_lat, my_lon], 
        tooltip='Your Location - Latitude: ' + str(my_lat) + 'Longitude: ' + str(my_lon)).add_to(m),
    # nearest weather station: 24.999447, 121.433812 
    # replace this with with (weather['lat'], weather['lon']) from find_nearest.py
    folium.Marker([weather['lat'], weather['lon']], 
        tooltip='Nearest Weather Location: ' + str(weather['lat']) + 'Longitude: ' + str(weather['lon']), 
        icon=folium.Icon(icon='cloud')).add_to(m),
    # generate map html
    m.save('templates/map.html')
    return render_template('map.html')

import os
# __main__ is the name of the current Python module.  
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)