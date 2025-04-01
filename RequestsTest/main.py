import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8a1ff71ef31e67cee98d0d32adb39e08'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {  
    "name": "Банан",
    "photo_id": 7
}

body_change = {
    "pokemon_id": "279288",
    "name": "Дыня",
    "photo_id": 3
}

body_pokeball = {
    "pokemon_id": "279288"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.json())

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.json())

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.json())


