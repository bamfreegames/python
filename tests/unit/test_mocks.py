from unittest.mock import patch
import pytest
import requests

def get_current_btc_price():
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    data = response.json()
    return data["bitcoin"]["usd"]


#tambien sirve @patch("requests.get") ya que estamos mockeando en nuestra propia funcion/modulo
@patch("requests.get")   # ruta completa del módulo donde se usa
def test_get_current_btc_price(mock_get):
    # Configurar qué devolverá el mock
    mock_get.return_value.json.return_value = {"bitcoin": {"usd": 50000}}
    
    # Ejecutar la función (internamente usa requests.get — que ahora es mock)
    result = get_current_btc_price()
    
    # Verificaciones
    assert result == 50000
    mock_get.assert_called_once()  # se llamó exactamente una vez

def get_btc_price_safe():
    """Versión con manejo de errores."""
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        response.raise_for_status()
        return response.json()["bitcoin"]["usd"]
    except requests.exceptions.RequestException:
        return None
    
# Test del happy path
@patch("requests.get")
def test_get_btc_price_success(mock_get):
    mock_get.return_value.json.return_value = {"bitcoin": {"usd": 50000}}
    mock_get.return_value.raise_for_status.return_value = None
    
    result = get_btc_price_safe()
    assert result == 50000

    # Test de error de red — imposible sin mock
@patch("requests.get")
def test_get_btc_price_network_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError("Network down")
    
    result = get_btc_price_safe()
    assert result is None  # manejó el error correctamente


# Test de error 500
@patch("requests.get")
def test_get_btc_price_server_error(mock_get):
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("500")
    
    result = get_btc_price_safe()
    assert result is None