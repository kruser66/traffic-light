import httpx

API_URL = 'http://127.0.0.1:8000/api/'


async def city_weather_request(city):
    _url = API_URL+f'weather?city={city}'

    async with httpx.AsyncClient() as client:
        response = await client.get(_url)

        response.raise_for_status()

        return response.json()
