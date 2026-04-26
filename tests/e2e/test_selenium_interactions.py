import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# <form id="order-form">
#     <select id="asset">
#         <option value="BTC">Bitcoin</option>
#         <option value="ETH">Ethereum</option>
#     </select>
    
#     <input type="number" id="amount" placeholder="0.00">
    
#     <button type="submit" id="submit-btn">Place Order</button>
# </form>

# <!-- Aparece DESPUÉS del click submit -->
# <div class="modal" id="confirm-modal" style="display: none;">
#     <h3>Confirm Your Order</h3>
#     <p>Buy <span id="confirm-amount">0.5</span> BTC</p>
#     <button id="confirm-btn">Confirm</button>
#     <button id="cancel-btn">Cancel</button>
# </div>

# <!-- Aparece DESPUÉS del confirm -->
# <div class="toast" id="success-toast" style="display: none;">
#     <p>Order placed successfully</p>
# </div>

#Escribe el código del test paso a paso — pero usando waits explícitos correctamente para:
def test_submit_order_check_dialogs(driver):
    #definimos el wait para luego
    wait = WebDriverWait(driver,10)
    
    # Seleccionar BTC
    select = Select(driver.find_element(By.ID, "asset"))
    select.select_by_value("BTC")
    
    # Escribir amount
    amount = driver.find_element(By.ID, "amount")
    amount.clear()
    amount.send_keys("0.5")
    
    # Click Place Order — esperar que sea clickable
    submit = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
    submit.click()
    
    # Esperar modal visible
    wait.until(EC.visibility_of_element_located((By.ID, "confirm-modal")))
    
    # Click Confirm
    confirm = wait.until(EC.element_to_be_clickable((By.ID, "confirm-btn")))
    confirm.click()
    
    # Esperar toast de éxito
    toast = wait.until(EC.visibility_of_element_located((By.ID, "success-toast")))
    
    # Verificar texto
    assert "successfully" in toast.text

def test_submit_multiple_orders(driver):
    wait = WebDriverWait(driver, 10)
    
    add_button = driver.find_element(By.ID, "add-order")
    
    # Añadir 3 órdenes y verificar después de cada click
    for i in range(3):
        add_button.click()
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, f".order-row[data-row-index='{i}']")
        ))
        rows = driver.find_elements(By.CSS_SELECTOR, ".order-row")
        assert len(rows) == i + 1
    
    # Eliminar la segunda fila (índice 1)
    row_to_delete = driver.find_element(
        By.CSS_SELECTOR, ".order-row[data-row-index='1']"
    )
    row_to_delete.find_element(By.CLASS_NAME, "delete-row").click()
    
    # Esperar que la fila desaparezca
    wait.until(EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, ".order-row[data-row-index='1']")
    ))
    
    # Verificar que quedan exactamente 2 filas y son las correctas
    remaining = driver.find_elements(By.CSS_SELECTOR, ".order-row")
    remaining_indices = [r.get_attribute("data-row-index") for r in remaining]
    
    assert len(remaining) == 2
    assert "0" in remaining_indices
    assert "2" in remaining_indices
    assert "1" not in remaining_indices