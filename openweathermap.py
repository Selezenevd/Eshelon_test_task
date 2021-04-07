import logging
import os
import requests
import json.decoder

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

BASE_URL_OWM = 'https://api.openweathermap.org/data/2.5/weather'
BASE_URL_WB = 'https://api.weatherbit.io/v2.0/current'
API_KEY_OPENWEATHERMAP = os.getenv('APPID')  #my API key (appid) from http://openweathermap.org
API_KEY_WEATHERBIT = os.getenv('API_MASTER_KEY')  #my API key (appid) from https://www.weatherbit.io/
NOT_AVAILABLE_MESSAGE = 'Запрашиваемый адрес недоступен: %s.'

app = FastAPI() 


@app.get('/weather')
def show_weather(city: str, country: str): 
    openweathermap_info = get_openweathermap_info(city)
    weatherbit_info = get_weatherbit_info(city, country)
    return {
        'openweathermap': openweathermap_info,
        'weatherbit': weatherbit_info,
    }


def get_request(query):
    try:
        response = requests.get(query)
        if response.status_code == 200:
            return response.json()      
    except requests.exceptions.RequestException as error:
        logging.debug('Запрашиваемый адрес недоступен: %s.', error)
    except json.decoder.JSONDecodeError as error:
        logging.debug('Ресурс вернул некорректный ответ')
    return None


def get_openweathermap_info(city):
    query = BASE_URL_OWM + f'?q={city}&units=metric&APPID={API_KEY_OPENWEATHERMAP}'
    return get_request(query)


def get_weatherbit_info(city, country):
    query = BASE_URL_WB + f'?city={city}&country={country}&key={API_KEY_WEATHERBIT}'
    return get_request(query)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
