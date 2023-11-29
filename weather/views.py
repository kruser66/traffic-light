
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response

from services.yandex import fetch_city_location, fetch_city_weather


class WeatherView(APIView):
    def get(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "city - обязательный параметр"}, status=400)

        cache_key = f"weather_{city}"
        weather = cache.get(cache_key, {})

        if not weather:
            location = fetch_city_location(city)
            if location:
                weather = fetch_city_weather(
                    latitude=location.latitude,
                    longitude=location.longitude
                    )
                weather['city'] = location.address
                cache_key = f"weather_{city}"
                cache.set(cache_key, weather, 30 * 60)
            else:
                weather['error'] = 'Неверное название города'

        return Response(weather)
