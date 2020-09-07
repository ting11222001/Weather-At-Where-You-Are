# Libraries for below main construction block - index function.
# Allow users to make a request to a web page e.g. an external API to get data.
import requests
# Transform a description of a location into such as a pair of coordinates.
import geocoder
# Use math module to access different mathematical functions.
import math

# Read the API keys from the .env file and use them
import os
from dotenv import load_dotenv
load_dotenv()

def find_nearest():
    # Insert government's API URL & parameters.
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization={}&format={}&elementName={}&parameterName={}'
    # insert arguments according to its API document.
    auth_arg = os.getenv('PROJECT_API_KEY')
    format_arg = 'JSON'
    ele_arg = 'TEMP,HUMD,24R'
    para_arg = 'CITY,TOWN'
    # Receive API data according to my specific arguments and it's in JSON format.
    req = requests.get(url.format(auth_arg, format_arg, ele_arg, para_arg)).json()
    # Next step is to find the nearest weather station in latitude and longitude versus my current location which is also in lat & lon.
    # Find location data from the returned JSON.
    data = req['records']['location']
    # Find where I am with geocoder.
    location = geocoder.ip('me').latlng
    my_lat = location[0]
    my_lon = location[1]
    # Append distances of each weather station versus my current location.
    result = []
    for location in data:
        any_lat = location['lat']
        any_lon = location['lon']
        p1 = [float(my_lat), float(my_lon)]
        p2 = [float(any_lat), float(any_lon)]
        distance = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
        result.append(distance)
    # Find the smallest values among all distances.
    nearest = min(result)
    # Get the index of the the smallest distance.
    nearest_index = result.index(nearest)
    # Get the data of the nearest weather station.
    nearest_location = data[nearest_index]
    # Pass this weather station's data as arguments from main.py to weather.html.
    weather = {
    'lat': nearest_location['lat'],
    'lon': nearest_location['lon'],
    'station_name': nearest_location['locationName'],
    'station_city': nearest_location['parameter'][0]['parameterValue'],
    'station_town': nearest_location['parameter'][1]['parameterValue'],
    'time': nearest_location['time']['obsTime'],
    'temperature': round(float(nearest_location['weatherElement'][0]['elementValue']), 0),
    'humidity': round(float(nearest_location['weatherElement'][1]['elementValue']) * 100, 0),
    'rainfall': nearest_location['weatherElement'][2]['elementValue'],
    }
    return weather, my_lat, my_lon
