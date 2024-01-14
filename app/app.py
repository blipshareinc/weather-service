from flask import Flask, request
from enum import Enum
from os import path

import json

app = Flask(__name__)

WEATHER_API_URL = "https://api.weather.gov/gridpoints"
GRID_POINTS = "LWX/103,83" # sample grid points

class ForeCast_Type(Enum):
    HOURLY = "%s/%s/%s" % (WEATHER_API_URL, GRID_POINTS, "forecast/hourly")    

class WeatherDotGovAPI:
    def __init__(self, forecast_type, lat, lon):
        self.forecast_type = forecast_type
        self.lat = lat
        self.lon = lon

    def fetch_data(self):
        # TODO: Implement the fetch but for now just the sample data for faster processing
        sample_data_file = path.join('../sample_data/city/hourly-forecast-output.json')
        with open(sample_data_file, 'r') as f:
            self.hourly_data = json.load(f)

        return self.hourly_data['properties']

@app.route("/")
def home():
    return "<h1 style='color:blue'>BLIPShare Home Automation Weather Service</h1>"

@app.route("/api/forecast/")
def get_hourly_forecast():
    query = request.args.to_dict(flat=False)
    print('query %s' % query)
    if not ("type" in query and "lat" and query and "lon" in query):
        return "API not available to process the requested \"%s\" query" % query

    forecast_type = query["type"][0]
    lat = float(query["lat"][0])
    lon = float(query["lon"][0])
    print("Type: %s, lat: %s, lon: %s" % (forecast_type, lat, lon))

    # load the sample data and return
    api = WeatherDotGovAPI(forecast_type, lat, lon)
    data = api.fetch_data()
    return f'Searching for: {data}'
