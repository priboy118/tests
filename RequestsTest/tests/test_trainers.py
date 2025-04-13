import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '512712b0d1d4e99d7218cf8c353351e1'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN } 
TRAINER_ID = '28597'

def test_get_trainers_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == "JOJO"
   

    
