import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.selenium.dev/selenium/web/locators_tests/locators.html"

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# TEST 1 — Verifica que el campo First Name tiene valor "Jane"
def test_first_name_value(driver):
    #accedemos a la url
    driver.get(URL)
    #encontramos el input de first name
    element = driver.find_element(By.ID, "fname")
    #seleccionamos el atributo value y comparamos con Jane
    assert element.get_attribute("value") == "Jane"

# TEST 2 — Selecciona el radio button Male
def test_select_male_radio(driver):
    #accedemos a la url
    driver.get(URL)
    #encontramos el radio button de male
    element = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][name="gender"][value="m"]')
    #lo seleccionamos
    element.click()
    #comprobamos si esta seleccionado
    assert element.is_selected() == True

# TEST 3 — Marca el checkbox Newsletter
def test_check_newsletter(driver):
    #accedemos a la url
    driver.get(URL)
    #encontramos el checkbox de la newsletter
    element = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="newsletter"]')
    #lo seleccionamos
    element.click()
    #comprobamos si esta seleccionado
    assert element.is_selected() == True

# TEST 4 — Verifica que el link de Selenium existe
def test_selenium_link_exists(driver):
    #accedemos a la url
    driver.get(URL)
    #encontramos el link
    element = driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")
    #comprobamos si existe el link
    assert element.get_attribute("href") != None

# TEST 5 — Verifica que el botón Submit existe y es clickable
def test_submit_button(driver):
    #accedemos a la url
    driver.get(URL)
    #encontramos el botón
    element = driver.find_element(By.CSS_SELECTOR, 'input[value="Submit"]')

    #encontramos el radio button de male
    gender_radio_element = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][name="gender"][value="m"]')
    #lo seleccionamos
    gender_radio_element.click()

    #encontramos el checkbox de la newsletter
    newsletter_cheeckbox_element = driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="newsletter"]')
    #lo seleccionamos
    newsletter_cheeckbox_element.click()

    #comprobamos que existe
    assert element.is_displayed() == True

    #comprobamos que es clickable tras marcar los campos necesarios por si fueran obligatorios
    assert element.is_enabled() == True


