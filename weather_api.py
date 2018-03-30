import requests

API_URL = 'http://api.openweathermap.org/data/2.5/weather?'


class WeatherAPI:

    def __init__(self, api_key):
        self.api_key = api_key

    def _call(self, query_string):
        r = requests.get(API_URL + query_string + "&units=metric" + "&APPID=" + self.api_key)
        return r.json()

    def get_weather_by_city(self, city_name):
        return self._call("q=" + city_name)


