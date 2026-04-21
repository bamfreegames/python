import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.selenium.dev/selenium/web/web-form.html"
URL_2 = "https://the-internet.herokuapp.com/dynamic_loading/1" 
URL_3 = "https://the-internet.herokuapp.com/tables"

@pytest.fixture
def driver():
    #service = Service(ChromeDriverManager().install())
    #driver = webdriver.Chrome(service=service)
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


#TEST 1 — Verifica que la tabla 1 tiene 4 filas
def test_verify_table1_rows(driver):
    driver.get(URL_3)
    element = driver.find_element(By.ID,"table1")
    table1_rows = element.find_elements(By.CSS_SELECTOR,'tbody tr')
    assert len(table1_rows) == 4

#TEST 2 — Verifica que "Smith" está en la primera fila de la tabla 1
def test_verify_table1_first_entry(driver):
    driver.get(URL_3)
    element = driver.find_element(By.ID,"table1")
    table1_rows = element.find_elements(By.CSS_SELECTOR,'tbody tr')
    # Get first element of tag 'td'
    #element_first_row_table1 = table1_rows[0].find_element(By.TAG_NAME, 'td')
    #get all elements from the first row
    elements_first_row_table1 = table1_rows[0].find_elements(By.TAG_NAME, 'td')
    assert elements_first_row_table1[0].text == "Smith"
    assert elements_first_row_table1[2].text == "jsmith@gmail.com"

#TEST 3 — Usando tabla 2 con clases, obtén el email de "Jason Doe"
def test_verify_email_person(driver):    
    #vamos a la url
    driver.get(URL_3)
    #encontramos la tabla
    element = driver.find_element(By.ID,"table2")
    #extraemos las filas con datos de clientes
    rows = element.find_elements(By.CSS_SELECTOR,'tbody tr')
    #recorremos las filas hasta encontrar un match en el nombre
    for r in rows:
        if r.find_element(By.CLASS_NAME,"first-name").text == "Jason" and r.find_element(By.CLASS_NAME,"last-name").text == "Doe":
            email = r.find_element(By.CLASS_NAME,"email").text
            break

    assert email == "jdoe@hotmail.com"

#TEST 4 — Encuentra la fila de "Tim Conway" y haz click en su link "edit"
def test_click_edit_person(driver):    
    #vamos a la url
    driver.get(URL_3)
    #encontramos la tabla
    element = driver.find_element(By.ID,"table2")
    #extraemos las filas con datos de clientes
    rows = element.find_elements(By.CSS_SELECTOR,'tbody tr')
    #recorremos las filas hasta encontrar un match en el nombre
    for r in rows:
        if r.find_element(By.CLASS_NAME,"first-name").text == "Tim" and r.find_element(By.CLASS_NAME,"last-name").text == "Conway":
            #hago click en edit
            edit_button = r.find_element(By.CSS_SELECTOR,'[href="#edit"]')
            edit_button.click()
            break

    assert "edit" in driver.current_url

#TEST 1 — Escribe texto en el Text input y verifica el valor
def test_text_input_value_using_css_selector(driver):
    breakpoint()
    #abrimos la pagina
    driver.get(URL)
    #encontramos el campo input por id
    element = driver.find_element(By.ID, "my-text-id")
    #limpiamos el campo y luego escribimos algo
    text = "borja adan"
    element.clear()
    element.send_keys(text)
    #comprobamos que el texto se ha escrito
    assert text in element.get_attribute("value")


#TEST 2 — Selecciona "Two" en el dropdown select
def test_select_option_in_dropdown(driver):
    #abrimos la pagina
    driver.get(URL)
    #encontramos el dropdown
    select_element = driver.find_element(By.NAME, 'my-select')
    select = Select(select_element)
    #encontramos el elemento a seleccionar
    select.select_by_value("2")
    #comprobamos
    assert select.first_selected_option.text == 'Two'

#TEST 3 — Verifica que el Disabled input no es editable
def test_verify_disabled_input(driver):    
    #abrimos la pagina
    driver.get(URL)
    #encontramos el input
    element = driver.find_element(By.CSS_SELECTOR, 'input[name="my-disabled"]')
    #comprobamos que esta deshabilitado
    assert element.is_enabled() == False

#TEST 4 — Verifica que el primer checkbox está marcado por defecto
def test_verify_checkbox_selected_default(driver):
    #abrimos la pagina
    driver.get(URL)
    #encontramos el campo input por id
    element = driver.find_element(By.ID, "my-check-1")
    #verificamos que esta seleccionada
    assert element.is_selected()

#TEST 5 — Desmarca el primer checkbox y verifica que quedó desmarcado
def test_verify_unchecked_checkbox(driver):
    #abrimos la pagina
    driver.get(URL)
    #encontramos el campo input por id
    element = driver.find_element(By.ID, "my-check-1")
    #click para deseleccionar
    element.click()
    #verificamos que esta desmarcado
    assert not element.is_selected()

# TEST — Click en Start y verifica que aparece Hello World
def test_dynamic_loading(driver):
    # 1. Ve a la página
    driver.get(URL_2)
    # 2. Encuentra el botón Start y haz click
    element = driver.find_element(By.XPATH, "//button[contains(text(),'Start')]")
    #print(f"Valor actual: + {element.text}")
    element.click()
    # 3. Espera explícitamente a que "Hello World" sea visible
    element_result = driver.find_element(By.ID, "finish")
    wait = WebDriverWait(driver, timeout=10)
    wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    #breakpoint()
    #wait.until(lambda _ : element_result.is_displayed())
    # 4. Verifica el texto
    assert "Hello World!" in element_result.text