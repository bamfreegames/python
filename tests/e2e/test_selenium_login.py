import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_using_css_selector(driver):
    # Usa CSS selectors para todos los elementos
    # 1. Ve a la página
    driver.get("https://www.selenium.dev/selenium/web/locators_tests/locators.html")
    element = driver.find_element(By.ID, "lname")    # 2. Encuentra username por CSS selector
    # 3. Encuentra password por CSS selector
    # 4. Encuentra el botón por CSS selector
    # 5. Verifica que llegaste a /secure
    
def test_login_successful(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Explicit wait para cambio de URL
    WebDriverWait(driver, 10).until(EC.url_contains("secure"))
    assert "secure" in driver.current_url

def test_login_empty_fields(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.error"))
    )
    assert "username is invalid" in error.text.lower()