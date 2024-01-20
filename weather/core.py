import requests
import json
from weather.utils import formatted_info

BASE_URL = 'https://api.weatherapi.com/v1/'
API_KEY = '9d7fece5e2454a6d895151548232505'


def search(place: str):
    url = BASE_URL + 'search.json?' + f'key={API_KEY}' + f'&q={place}'

    response = requests.get(url)

    if response.status_code != 200:
        return []

    return json.loads(response.text)


def get_weather(place):
    url = BASE_URL + 'current.json?' + f'key={API_KEY}' + f'&q={place}'

    response = requests.get(url)

    if response.status_code != 200:
        return 'No data found!'

    data = json.loads(response.text)

    return formatted_info(data)
