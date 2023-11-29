import httpx
from config.settings import API_URL


async def city_weather_request(city):
    _url = API_URL+f'weather?city={city}'

    async with httpx.AsyncClient() as client:
        response = await client.get(_url)

        response.raise_for_status()

        return response.json()
