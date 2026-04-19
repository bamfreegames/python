# pages/login_page_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    URL = "https://the-internet.herokuapp.com/login"

    #locators
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    error_message = (By.CSS_SELECTOR, ".flash.error")
    success_message = (By.CSS_SELECTOR, ".flash.success")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def goto(self):
        # navega a la URL
        self.driver.get(self.URL)

    def login(self, username, password):
        # encuentra username, password y botón
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        # escribe las credenciales y hace click

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        )
        return error.text

    def is_login_successful(self):
        self.wait.until(EC.url_contains("secure"))
        return "secure" in self.driver.current_url
    
    def get_success_message(self):
        success = self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        )
        return success.text
    
    def get_page_title(self):
        return self.driver.title
