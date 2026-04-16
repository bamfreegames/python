import pytest
from playwright.sync_api import Page, expect

class TestLocators:

    def test_page_loads(self, page: Page):
        page.goto("https://the-internet.herokuapp.com")
        expect(page).to_have_title("The Internet")

    def test_login_by_label(self, page: Page):
        page.goto("https://the-internet.herokuapp.com/login")
        # Por label — busca el elemento asociado al label "Username"
        page.get_by_label("Username").fill("tomsmith")
        page.get_by_label("Password").fill("SuperSecretPassword!")
        page.get_by_role("button", name="Login").click()
        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

    def test_login_by_placeholder(self, page: Page):
        page.goto("https://the-internet.herokuapp.com/login")
        # Por placeholder — el texto gris dentro del campo
        page.get_by_placeholder("Username").fill("tomsmith")
        page.get_by_placeholder("Password").fill("SuperSecretPassword!")
        page.get_by_role("button", name="Login").click()
        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

    def test_login_by_css(self, page: Page):
        page.goto("https://the-internet.herokuapp.com/login")
        # Por CSS selector — usando el id del elemento
        page.locator("#username").fill("tomsmith")
        page.locator("#password").fill("SuperSecretPassword!")
        page.locator("button[type='submit']").click()
        expect(page).to_have_url("https://the-internet.herokuapp.com/secure")

    def test_login_failed(self, page: Page):
        page.goto("https://the-internet.herokuapp.com/login")
        # Negative case — credenciales incorrectas
        page.get_by_label("Username").fill("wronguser")
        page.get_by_label("Password").fill("wrongpassword")
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_role("alert")).to_be_visible()