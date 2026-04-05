import requests
from config import Config

#словарь для корректного отображения названия типа погоды на сайте
condition_translations = {
    "Partly cloudy": "Переменная облачность",
    "Cloudy": "Облачно",
    "Overcast": "Пасмурно",
    "Sunny": "Солнечно",
    "Clear": "Ясно",
    "Mist": "Туман",
    "Patchy rain nearby": "Местами дождь",
    "Light rain": "Небольшой дождь",
    "Moderate rain": "Умеренный дождь",
    "Heavy rain": "Сильный дождь",
    "Light snow": "Небольшой снег",
    "Moderate snow": "Умеренный снег",
    "Heavy snow": "Сильный снег",
}


class WeatherService:
    def __init__(self):
        self.api_key = Config.WEATHER_API_KEY
        self.base_url = 'https://api.weatherapi.com/v1/current.json'

    def weather_request_base(self, city='Moscow'):
        params = {
            'key': self.api_key,
            'q': city,
            'aqi': 'no'
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()

            data = response.json()

            condition_en = data["current"]["condition"]["text"]
            condition_ru = condition_translations.get(condition_en, condition_en)

            return {
                "temperature": data["current"]["temp_c"],
                "condition": condition_ru,
                "city": data["location"]["name"]
            }

        except requests.exceptions.RequestException as err:
            print("Request Error:", err)
            return None