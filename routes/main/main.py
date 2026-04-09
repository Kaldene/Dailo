from flask import blueprints,render_template
from datetime import datetime
from service.weather_service import WeatherService

main_routes = blueprints.Blueprint('main', __name__)

@main_routes.route('/home')
@main_routes.route('/')
def home():
    now=datetime.now()

    months = {
        1: "Января",
        2: "февраля",
        3: "Марта",
        4: "Апреля",
        5: "Мая",
        6: "Июня",
        7: "Июля",
        8: "Августа",
        9: "Сентября",
        10: "Октября",
        11: "Ноября",
        12: "Декабря",
    }

    weather_service = WeatherService()
    current_weather_base = weather_service.weather_request_base("Москва")

    current_day = now.day
    current_month = months[now.month]

    return render_template('main/index.html',
                           current_day=current_day,
                           current_month=current_month,
                           current_weather_base=current_weather_base)