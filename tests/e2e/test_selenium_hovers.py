import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/hovers"

@pytest.fixture
def driver():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# TEST 1 — Hover sobre user1 y verifica caption
def test_hover_shows_caption(driver):
    driver.get(URL)
    figure = driver.find_element(By.XPATH, "(//div[@class='figure'])[1]")
    
    ActionChains(driver).move_to_element(figure).perform()
    
    caption = figure.find_element(By.CLASS_NAME, "figcaption")
    assert caption.is_displayed()
    assert "name: user1" in caption.text


# TEST 2 — Hover sobre user2 y click en "View profile"
def test_hover_and_click_profile(driver):
    driver.get(URL)
    figure = driver.find_element(By.XPATH, "(//div[@class='figure'])[2]")
    
    ActionChains(driver).move_to_element(figure).perform()
    
    figure.find_element(By.LINK_TEXT, "View profile").click()
    assert "/users/2" in driver.current_url


# TEST 3 — Caption NO visible sin hover
def test_caption_hidden_without_hover(driver):
    driver.get(URL)
    figure = driver.find_element(By.XPATH, "(//div[@class='figure'])[1]")
    caption = figure.find_element(By.CLASS_NAME, "figcaption")
    
    assert not caption.is_displayed()