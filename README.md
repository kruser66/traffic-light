# API "Погода от Яндекса" (тестовое задание)

- Реализовать API получение погоды в городе с сервиса Яндекс (температура, давление и ветер)

```yaml
GET weather?city=<city_name>
```

- Организаовать кеширование данных (при повторном запросе в течении 30 минут - запросы к Яндекс не должны идти)
- Реализовать бот, которому указать название города и он обращается к созданному API и выводит информацию по данному городу

## Как установить

Python 3 должен быть установлен.

- Скачать проект (git clone)

- Создать виртуальное окружение.

```bash
python -m venv venv
```

- Установить зависимости.

```bash
pip install -r requirements.txt
```

Для запуска проекта понадобятся переменные окружения:

```bash
BOT_TOKEN='YOUR_BOT_TOKEN'
SECRET_KEY='DJANGO_SECRET_KEY'

YANDEX_GEO_AI_KEY='API_YANDEX_GEO'
YANDEX_WEATHER_API_KEY='API_YANDEX_WEATHER'
```

## Запуск проекта

Запускаем сервер для работы API:

```bash
python manage.py runserver
```

Запускаем бот:

```bash
python bot.py
```

### Доступные endpoints

GET /api/weather?city=<city_name>

## Цель проекта

Выполнение тестового задания на вакансию Middle Python разработчик
