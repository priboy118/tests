import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '512712b0d1d4e99d7218cf8c353351e1'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN } 

body_create = {"name": "Жидкий","photo_id": -1}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json= body_create)


print(response_create.status_code) 

body_response = response_create.json()
MESSAGE = body_response['message']
ID = body_response['id']
print(MESSAGE, ID)




