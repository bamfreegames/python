# tests/e2e/test_login_pom.py
import pytest
from pages.login_page_selenium import LoginPage

class TestLoginPOM:

    def test_valid_login(self, driver):
        # usa LoginPage para hacer login correcto
        login = LoginPage(driver)
        login.goto()
        # verifica que el login fue exitoso
        login.login("tomsmith","SuperSecretPassword!")
        assert login.is_login_successful() == True

    def test_invalid_login(self, driver):
        login = LoginPage(driver)
        login.goto()
        # usa LoginPage para hacer login incorrecto
        login.login("a","a")
        # verifica el mensaje de error
        assert "invalid" in login.get_error_message()

    def test_login_page_title(self, driver):
        # verifica que el título de la página es correcto
        login = LoginPage(driver)
        login.goto()
        assert "The Internet" in login.get_page_title()