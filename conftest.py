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

#this is just a comment to test
#that I can retrieve a change in local from remote repo

<<<<<<< HEAD
#prueba para fetch
=======
#me equivoque
>>>>>>> main
