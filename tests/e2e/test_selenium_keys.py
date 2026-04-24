import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

URL = "https://the-internet.herokuapp.com/key_presses"
URL_2 = "https://the-internet.herokuapp.com/inputs"

@pytest.fixture
def driver():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#Ejercicio 1 — Escribir texto y seleccionar todo con Cmd+A
def test_cmd_a_select(driver):
    driver.get(URL_2)
    input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
    input.click()
    input.send_keys("5")
    
    # Cmd+A para seleccionar todo
    ActionChains(driver)\
        .key_down(Keys.COMMAND)\
        .send_keys("a")\
        .key_up(Keys.COMMAND)\
        .perform()
    
    # Escribir algo nuevo si la selección funciona, reemplaza
    input.send_keys("99")
    
    assert "99" in input.get_attribute("value")  

#Ejercicio 2 — Escribir texto, seleccionar y borrar con Delete
def test_cmd_a_delete(driver):
    driver.get(URL_2)
    input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
    input.click()
    input.send_keys("5")
    
    # Cmd+A para seleccionar todo y borrar DELETE
    ActionChains(driver)\
        .key_down(Keys.COMMAND)\
        .send_keys("a")\
        .key_up(Keys.COMMAND)\
        .send_keys(Keys.DELETE)\
        .perform()
    
    assert input.get_attribute("value") == ""

#Ejercicio 3 — Copiar + pegar con Cmd+C / Cmd+V "Hello"
def test_cmd_c_v(driver):
    driver.get(URL_2)
    input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
    input.click()
    input.send_keys("5")
    
    # Cmd+C para copiar
    ActionChains(driver)\
        .key_down(Keys.COMMAND)\
        .send_keys("a")\
        .key_up(Keys.COMMAND)\
        .key_down(Keys.COMMAND)\
        .send_keys("c")\
        .key_up(Keys.COMMAND)\
        .key_down(Keys.RIGHT)\
        .key_down(Keys.COMMAND)\
        .send_keys("v")\
        .key_up(Keys.COMMAND)\
        .perform()
    
    assert input.get_attribute("value") == "55"

#TEST 1 — Pulsa ENTER y verifica "You entered: ENTER"
def test_click_enter(driver):
    #vamos a la url
    driver.get(URL)
    #encuentro el input
    result = driver.find_element(By.ID,"result")
    #input key
    input = driver.find_element(By.ID,"target")
    input.click()
    input.send_keys(Keys.ENTER)
    #ActionChains(driver)\
    #    .key_down(Keys.ENTER)\
    #    .perform()
    assert "ENTER" in result.text


