import pytest
import requests
import time

BASE_URL = "https://api.coingecko.com/api/v3"

@pytest.fixture
def btc_price_response():
    time.sleep(1)  # respeta el rate limit
    response = requests.get(
        f"{BASE_URL}/simple/price",
        params={"ids": "bitcoin", "vs_currencies": "usd"}
    )
    return response

class TestCryptoAPI:

    @pytest.mark.api
    @pytest.mark.smoke
    def test_api_returns_200(self, btc_price_response):
        assert btc_price_response.status_code == 200

    @pytest.mark.api
    def test_bitcoin_price_is_positive(self, btc_price_response):
        data = btc_price_response.json()
        assert data["bitcoin"]["usd"] > 0

    @pytest.mark.api
    def test_response_contains_bitcoin_key(self, btc_price_response):
        data = btc_price_response.json()
        assert "bitcoin" in data

    @pytest.mark.api
    @pytest.mark.parametrize("coin", ["bitcoin", "ethereum"])
    def test_multiple_coins_return_price(self, coin):
        time.sleep(2)  # más delay para parametrize
        response = requests.get(
            f"{BASE_URL}/simple/price",
            params={"ids": coin, "vs_currencies": "usd"}
        )
        data = response.json()
        assert response.status_code == 200
        assert data[coin]["usd"] > 0

    @pytest.mark.api
    def test_invalid_coin_returns_empty(self):
        time.sleep(2)
        response = requests.get(
            f"{BASE_URL}/simple/price",
            params={"ids": "notacoin", "vs_currencies": "usd"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data == {}