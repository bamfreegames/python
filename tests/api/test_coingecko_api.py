import pytest
import requests

BASE_URL = "https://api.coingecko.com/api/v3"
BASE_URL_2 = "https://api.coingecko.com/api/v3/coins/list"
URL = "https://jsonplaceholder.typicode.com/posts"
URL_2 = "https://jsonplaceholder.typicode.com/posts/1"

def test_put():
    #Haga el PUT
    body = {"id": 1,"title": "Updated title","body": "Updated body","userId": 1}
    response = requests.put(URL_2,json=body)
    #Verifique status 200
    assert response.status_code==200
    data = response.json()
    #Verifique que el campo title es "Updated title"
    assert data["title"] == "Updated title"
    #Verifique que el campo id sigue siendo 1
    assert data["id"] == 1

def test_post():
    #Haga el POST con el body JSON
    breakpoint()
    data = {"title": "Test from Borja","body": "This is a test post","userId": 1}
    response = requests.post(URL, json=data)
    #Verifique status 201
    assert response.status_code==201
    #Verifique que la respuesta contiene un campo id
    result=response.json()
    assert "id" in result
    #Verifique que los campos enviados se reflejan en la respuesta
    assert result["title"] == "Test from Borja"
    assert result["body"] == "This is a test post"
    assert result["userId"] == 1

@pytest.mark.parametrize("coin,name,symbol", [
    ("bitcoin", "Bitcoin", "btc"),
    ("ethereum", "Ethereum", "eth"),
    ("tether", "Tether", "usdt"),
    ("solana", "Solana", "sol"),
])

def test_bitcoin_price(coin,name,symbol):
    #Haga la petición
    url = f"{BASE_URL}/coins/{coin}"
    response = requests.get(url)
    #Verifique status 200
    assert response.status_code==200
    data = response.json() 
    #Verifique que el campo name es "Bitcoin"
    assert data['name'] == name
    #Verifique que el campo symbol es "btc"
    assert data['symbol'] == symbol
    #Verifique que market_data.current_price.usd existe y es positivo
    usd_price = data['market_data']['current_price']['usd']
    assert usd_price is not None
    assert usd_price > 0

def test_get_coins():
    response = requests.get(BASE_URL_2)
    assert response.status_code == 200
    
    data = response.json()
    
    # TEST 2 — Lista tiene más de 10.000 elementos
    assert len(data) > 10000
    
    # TEST 3 — Bitcoin está en la lista
    assert any(coin['id'] == 'bitcoin' for coin in data)
    
    # TEST 4 — Cada elemento tiene id, symbol y name
    required_keys = {"id", "symbol", "name"}
    assert all(required_keys.issubset(coin.keys()) for coin in data)



def test_get_bitcoin_price():
    # 1. Construir la URL
    url = f"{BASE_URL}/simple/price"
    # 2. Construir los parámetros
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }
    # 3. Hacer la petición
    response = requests.get(url, params=params)
    # 4. Verificar status code
    assert response.status_code == 200
    # 5. Parsear JSON
    data = response.json()
    # 6. Verificar estructura
    #Que existe la clave "bitcoin"
    assert "bitcoin" in data
    assert "bitcoin" in data.keys()
    #Que bitcoin tiene la clave "usd"
    assert "usd" in data['bitcoin']
    assert "usd" in data['bitcoin'].keys()
    #Que el precio es un número positivo
    assert data['bitcoin']['usd'] > 0