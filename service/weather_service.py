import requests
from config import Config


class WeatherService:
    def __init__(self):
        self.api_key = Config.WEATHER_API_KEY
        self.base_url = 'http://api.weatherapi.com/v1'


