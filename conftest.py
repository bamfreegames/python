import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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

@pytest.fixture
def driver():
    # SETUP — crea el driver antes del test
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#this is just a comment to test
#that I can retrieve a change in local from remote repo

#me equivoque
#vale ya lo entiendo jeje
