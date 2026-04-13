import pytest

@pytest.fixture
def valid_order():
    return {
        "amount": 0.5,
        "asset": "BTC",
        "side": "buy"
    }

@pytest.fixture
def invalid_order():
    return {
        "amount": -1,
        "asset": "LINK",
        "side": "hold"
    }