from time import sleep

import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/infinite_scroll"
URL_2 = "https://the-internet.herokuapp.com/redirector"
URL_3 = "https://the-internet.herokuapp.com/login"


#TEST 1 — Screenshot básico de la página de login
def test_screenshot_completo(driver):
    #Ve a la página de login
    driver.get(URL_3)
    #Captura screenshot de la página completa
    screenshot_name="full_page_screenshot.png"
    driver.save_screenshot(screenshot_name)
    #Verifica que el archivo existe en disco
    assert os.path.exists(screenshot_name) 
    assert os.path.getsize(screenshot_name) > 0

#TEST 2 — Screenshot de un elemento específico
def test_screenshot_element(driver):
    #Ve a la página de login
    driver.get(URL_3)
    #Encuentra el campo username
    element = driver.find_element(By.ID,"username")
    #Captura screenshot solo del input
    screenshot_path = "username_input.png"
    result = element.screenshot(screenshot_path)
    # Verifica
    assert result == True
    assert os.path.exists(screenshot_path)

#TEST 1 — Click en el link y verifica la redirección a status_codes
def test_redirection(driver):
    driver.get(URL_2)
    breakpoint()
    element = driver.find_element(By.ID,"redirect")
    element.click()
    wait = WebDriverWait(driver,10)
    wait.until(EC.url_contains("status_codes"))
    assert "status_codes" in driver.current_url
    


# TEST 1 — Verifica que el scroll infinito carga nuevos párrafos
def test_complete_navigation_flow(driver):
    wait = WebDriverWait(driver,5)
    #Ve a la URL
    driver.get(URL)
    #Cuenta cuántos párrafos hay inicialmente (p.large-12.columns o .jscroll-added)
    paragraphs = driver.find_elements(By.CSS_SELECTOR,'div[class="jscroll-added"]')
    initial_count=len(paragraphs)
    #Haz scroll al final de la página
    ActionChains(driver)\
        .scroll_to_element(paragraphs[-1])\
        .perform()
    #Espera 2-3 segundos para que cargue
    sleep(3)
    #Cuenta de nuevo
    after_count = len(driver.find_elements(By.CSS_SELECTOR,'div[class="jscroll-added"]'))
    #Verifica que hay más párrafos que al principio
    assert after_count > initial_count