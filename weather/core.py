import requests
import json

BASE_URL = 'https://api.weatherapi.com/v1/'
API_KEY = '9d7fece5e2454a6d895151548232505'


def search(place: str):
    url = BASE_URL + 'search.json?' + f'key={API_KEY}' + f'&q={place}'

    response = requests.get(url)

    return json.loads(response.text)


def get_weather():
    pass
