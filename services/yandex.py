import httpx
from geopy.geocoders import Yandex


from config.settings import YANDEX_GEO_AI_KEY
from config.settings import YANDEX_WEATHER_API_KEY


def fetch_city_location(city):

    yandex_geocoder = Yandex(YANDEX_GEO_AI_KEY)

    return yandex_geocoder.geocode(city)


def fetch_city_weather(latitude, longitude):
    weather_url = 'https://api.weather.yandex.ru/v2/forecast'
    weather = {}

    with httpx.Client() as client:
        response = client.get(
            f'{weather_url}?lat={latitude}&lon={longitude}&lang=ru_RU',
            headers={'X-Yandex-API-Key': YANDEX_WEATHER_API_KEY}
        )

        response.raise_for_status()
        fact = response.json()['fact']
        weather = {
            'temp': fact['temp'],
            'pressure_mm': fact['pressure_mm'],
            'wind_speed': fact['wind_speed'],
        }

    return weather
