import httpx
from geopy.geocoders import Yandex
from geopy.adapters import AioHTTPAdapter

from config.settings import YANDEX_GEO_AI_KEY
from config.settings import YANDEX_WEATHER_API_KEY


async def fetch_city_location(city):

    async with Yandex(
        YANDEX_GEO_AI_KEY,
        adapter_factory=AioHTTPAdapter
    ) as yandex_geocoder:

        return await yandex_geocoder.geocode(city)


async def fetch_city_weather(latitude, longitude):
    weather_url = 'https://api.weather.yandex.ru/v2/forecast'

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f'{weather_url}?lat={latitude}&lon={longitude}&lang=ru_RU',
            headers={'X-Yandex-API-Key': YANDEX_WEATHER_API_KEY}
        )

        response.raise_for_status()

    return response.json()['fact']
