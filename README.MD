# Описание проекта 

Это тестовое задание для компании НПО "Эшелон".

С двух API необходимо получить весь список значений для указанного города.
https://openweathermap.org/current#current_JSON
https://www.weatherbit.io/api/swaggerui/weather-api-v2#!/Current32Weather32Data/get_current_city_id_city_id

Затем предоставить route для GET-запроса.

## Как развернуть проект

1. Склонировать репозиторий.
2. Создать окружение: python3 -m venv venv
3. Активировать окружение: source venv/bin/activate
4. Запустить команду 'pip install -r requirements.txt'

## Как запустить проект:
1. В терминале запустить команду 'python openweathermap.py'
2. В браузере открыть ссылку 'http://127.0.0.1:8000/docs'
3. В открывшемся интерфейсе кликнуть по панели синего цвета "GET".
4. Нажать "Try it out".
5. Ввести значения CITY и COUNTRY и нажать "EXECUTE".
