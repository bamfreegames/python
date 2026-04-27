import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/windows"

@pytest.fixture
def driver():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#TEST 1 — Click en el link, cambia a la nueva pestaña, verifica el texto "New Window" y cierra
def test_click_navigate_new_window(driver):
    #vamos a la url
    driver.get(URL)
    # Setup wait for later
    wait = WebDriverWait(driver, 10)
    # Store the ID of the original window
    original_window = driver.current_window_handle
    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1
    #encontramos el link
    element = driver.find_element(By.LINK_TEXT, "Click Here")
    #hacemos click
    element.click()
    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("New Window"))
    #cogemos el texto de la nueva pestana
    text = driver.find_element(By.TAG_NAME,'h3').text
    #cerramos la pestaña
    #Close the tab or window
    driver.close()
    #Switch back to the old tab or window
    driver.switch_to.window(original_window)
    assert "The Internet" in driver.title
    assert "New Window" in text


# # Guardar la ventana actual
# original = driver.current_window_handle

# # Esperar a que se abra una nueva
# wait.until(EC.number_of_windows_to_be(2))

# # Cambiar a la nueva
# for handle in driver.window_handles:
#     if handle != original:
#         driver.switch_to.window(handle)
#         break

# # Hacer cosas en la nueva ventana
# driver.find_element(By.ID, "...").click()

# # Cerrar la actual y volver
# driver.close()
# driver.switch_to.window(original)