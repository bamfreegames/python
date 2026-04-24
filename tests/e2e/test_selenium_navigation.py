import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/"

@pytest.fixture
def driver():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


#     TEST 1 — Flujo completo de navegación
def test_complete_navigation_flow(driver):
    wait = WebDriverWait(driver, 10)
    
    # 1. Ve a la home
    driver.get(URL)
    assert driver.current_url == "https://the-internet.herokuapp.com/"
    
    # 2. Click en A/B Testing
    driver.find_element(By.PARTIAL_LINK_TEXT, "A/B").click()
    wait.until(EC.url_contains("abtest"))
    assert "abtest" in driver.current_url
    
    # 3. Atrás
    driver.back()
    wait.until(EC.url_to_be("https://the-internet.herokuapp.com/"))
    assert driver.current_url == "https://the-internet.herokuapp.com/"
    
    # 4. Adelante
    driver.forward()
    wait.until(EC.url_contains("abtest"))
    assert "abtest" in driver.current_url
    
    # 5. Refresh
    driver.refresh()
    wait.until(EC.url_contains("abtest"))
    assert "abtest" in driver.current_url