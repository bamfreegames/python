from unittest.mock import patch
import pytest
import requests

def get_current_btc_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    data = response.json()
    return data["bitcoin"]["usd"]


@patch("tests.unit.test_mocks.requests.get")   # ruta completa del módulo donde se usa
def test_get_current_btc_price(mock_get):
    # Configurar qué devolverá el mock
    mock_get.return_value.json.return_value = {"bitcoin": {"usd": 50000}}
    
    # Ejecutar la función (internamente usa requests.get — que ahora es mock)
    result = get_current_btc_price()
    
    # Verificaciones
    assert result == 50000
    mock_get.assert_called_once()  # se llamó exactamente una vez