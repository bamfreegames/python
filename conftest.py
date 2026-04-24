import pytest
from datetime import datetime
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
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def driver_headless():
    # SETUP — crea el driver antes del test
    service = Service(ChromeDriverManager().install())
    #headless
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options = options, service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#this is just a comment to test
#that I can retrieve a change in local from remote repo

#me equivoque
#vale ya lo entiendo jeje

# conftest.py

#@pytest.fixture(autouse=True)
@pytest.fixture()
def capture_screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        test_name = request.node.name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(filename)
        print(f"\nScreenshot saved: {filename}")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)