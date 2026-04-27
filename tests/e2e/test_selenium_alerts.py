import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/javascript_alerts"

@pytest.fixture
def driver():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#TEST 2 — JS Confirm — cancela (dismiss) y verifica "You clicked: Cancel"

def test_click_js_confirm_and_dismiss(driver):
    #ir a la url
    driver.get(URL)
    #encontrar el elemento
    element=driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']")
    #hacemos click
    element.click()
    #saltamos la alerta
    alert = driver.switch_to.alert
    alert.dismiss()
    #comprobamos el resultado
    assert "You clicked: Cancel" in driver.find_element(By.ID,"result").text

#TEST 1 — JS Alert — acepta y verifica el mensaje "You successfully clicked an alert"
def test_click_js_alert(driver):
    #ir a la url
    driver.get(URL)
    #encontrar el elemento
    element=driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']")
    #hacemos click
    element.click()
    #saltamos la alerta
    wait = WebDriverWait(driver, timeout=5)
    #alert = wait.until(EC.alert_is_present())
    alert = wait.until(lambda d : d.switch_to.alert)
    text = alert.text
    alert.accept()
    #comprobamos el resultado
    assert "You successfully clicked an alert" in driver.find_element(By.ID,"result").text


#TEST 3 — JS Confirm — acepta y verifica "You clicked: Ok"

def test_click_js_confirm_and_accept(driver):
    #ir a la url
    driver.get(URL)
    #encontrar el elemento
    element=driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']")
    #hacemos click
    element.click()
    #saltamos la alerta
    alert = driver.switch_to.alert
    alert.accept()
    #comprobamos el resultado
    assert "You clicked: Ok" in driver.find_element(By.ID,"result").text

#TEST 4 — JS Prompt — escribe "Borja QA" y acepta. Verifica "You entered: Borja QA"
def test_click_js_prompt_and_check(driver):
    #ir a la url
    driver.get(URL)
    #encontrar el elemento
    element=driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")
    #hacemos click
    element.click()
    #saltamos la alerta
    alert = driver.switch_to.alert
    alert.send_keys("Borja QA")
    alert.accept()
    #comprobamos el resultado
    assert "You entered: Borja QA" in driver.find_element(By.ID,"result").text



