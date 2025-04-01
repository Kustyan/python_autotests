import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TRAINER_ID = '32834'

def test_status_code():
    response_get = requests.get(url= f'{URL}/trainers')
    assert response_get.status_code == 200

def test_contains_my_trainer():
    response_get_contains = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get_contains.json()['data'][0]['trainer_name'] == 'Kust'

'''Ниже использовал параметризацию, проверил сразу, что ответ содержит имя моего тренера, уровень и город Екатеринбург'''

@pytest.mark.parametrize('key, value', [('trainer_name', 'Kust'), ('level', '5'), ('city', 'Екатеринбург')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url= f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value
