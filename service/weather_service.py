import requests
from config import Config


class WeatherService:

    def __init__(self):
        self.api_key = Config.WEATHER_API_KEY
        self.base_url = 'http://api.weatherapi.com/v1/current.json'

    """
    Получение данных о погоде в москве
    :return температура в цельсиях, тип погоды 
    """
    def weather_request_base(self, city='Moscow'):

        params = {
            'key': self.api_key,
            'q': city,
            'aqi': 'no'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()

            data = response.json()

            return (
                data["current"]["temp_c"],
                data["current"]["condition"]["text"],
                data["location "]["name"]
            )
        except requests.exceptions.HTTPError as errh:
            print('Http Error:', errh)
            return None

