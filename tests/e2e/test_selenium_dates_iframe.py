import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

#<input type="date" id="birthdate">
#driver.find_element(By.ID, "birthdate").send_keys("12/31/2026")



# <input id="date-input" readonly>     <!-- el input es readonly -->
# <div class="calendar-popup">
#     <button class="prev-month">‹</button>
#     <span class="month">December 2026</span>
#     <button class="next-month">›</button>
#     <table class="calendar-grid">
#         <tr>
#             <td class="day">1</td>
#             <td class="day">2</td>
#             ...
#             <td class="day selected">15</td>
#         </tr>
#     </table>
# </div>

def select_date(driver, target_year, target_month, target_day):
    # 1. Click en el input para abrir el calendario
    driver.find_element(By.ID, "date-input").click()
    
    # 2. Esperar que el calendario sea visible
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "calendar-popup")))
    
    # 3. Navegar al mes correcto (clicks en flechas)
    while True:
        current_month_text = driver.find_element(By.CLASS_NAME, "month").text
        if f"{target_month} {target_year}" in current_month_text:
            break
        driver.find_element(By.CLASS_NAME, "next-month").click()
    
    # 4. Click en el día deseado
    day_locator = (By.XPATH, f"//td[@class='day' and text()='{target_day}']")
    driver.find_element(*day_locator).click()




# #Forzar el valor del input vía JavaScript
# driver.execute_script(
#     "document.getElementById('date-input').value = '2026-12-31'"
# )


# <select name="month">
#     <option value="12">December</option>
# </select>
# <select name="year">
#     <option value="2026">2026</option>
# </select>
# <select name="day">
#     <option value="31">31</option>
# </select>

def select_date_dropdown(driver):
    Select(driver.find_element(By.NAME, "month")).select_by_value("12")
    Select(driver.find_element(By.NAME, "year")).select_by_value("2026")
    Select(driver.find_element(By.NAME, "day")).select_by_value("31")


#     <html>
#     <body>
#         <h1>Página principal</h1>
        
#         <iframe id="payment-frame" src="https://payments.com">
#             <!-- DOM completamente separado dentro -->
#             <html>
#                 <body>
#                     <input id="card-number">     ← Selenium NO ve esto desde fuera
#                 </body>
#             </html>
#         </iframe>
#     </body>
# </html>


# # Opción 1 — por nombre o ID
# driver.switch_to.frame("payment-frame")

# # Opción 2 — por índice (orden de aparición)
# driver.switch_to.frame(0)

# # Opción 3 — por elemento (más robusto)
# iframe = driver.find_element(By.ID, "payment-frame")
# driver.switch_to.frame(iframe)



# # Volver al documento principal
# driver.switch_to.default_content()

# # Subir UN nivel (si hay iframes anidados)
# driver.switch_to.parent_frame()



# wait.until(EC.frame_to_be_available_and_switch_to_it(
#     (By.ID, "payment-frame")
# ))
# # Ya estás dentro del frame, puedes interactuar





def test_payment_form_in_iframe(driver):
    driver.get("https://example.com/checkout")
    
    # 1. Cambiar al iframe
    driver.switch_to.frame("payment-frame")
    
    # 2. Ahora puedes interactuar con elementos DENTRO del iframe
    driver.find_element(By.ID, "card-number").send_keys("4111111111111111")
    driver.find_element(By.ID, "submit").click()
    
    # 3. Volver al documento principal antes de seguir con la página
    driver.switch_to.default_content()
    
    # 4. Continúas con elementos de la página principal
    success = driver.find_element(By.CLASS_NAME, "success-message")
    assert success.is_displayed()
