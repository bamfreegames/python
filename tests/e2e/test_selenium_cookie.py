import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

URL = "https://the-internet.herokuapp.com/login"

@pytest.fixture
def driver():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# TEST 1 — Obtener y mostrar todas las cookies iniciales
def test_get_all_cookies(driver):
    driver.get(URL)
    cookies = driver.get_cookies()
    
    assert isinstance(cookies, list)
    print(f"\nCookies encontradas: {len(cookies)}")
    for cookie in cookies:
        print(f"  {cookie['name']} = {cookie['value']}")


# TEST 2 — Añadir una cookie personalizada y verificarla
def test_add_custom_cookie(driver):
    driver.get(URL)
    
    new_cookie = {
        "name": "test_user",
        "value": "borja_qa"
    }
    driver.add_cookie(new_cookie)
    
    # Recuperarla
    retrieved = driver.get_cookie("test_user")
    
    assert retrieved is not None
    assert retrieved["name"] == "test_user"
    assert retrieved["value"] == "borja_qa"


# TEST 3 — Eliminar una cookie específica
def test_delete_cookie(driver):
    driver.get(URL)
    
    # Añade primero
    driver.add_cookie({"name": "temp", "value": "delete_me"})
    assert driver.get_cookie("temp") is not None
    
    # Elimínala
    driver.delete_cookie("temp")
    
    # Verifica que ya no existe
    assert driver.get_cookie("temp") is None