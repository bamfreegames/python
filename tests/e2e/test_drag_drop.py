import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains

#option 1
# source = driver.find_element(By.ID, "card-1")
# target = driver.find_element(By.ID, "done-column")

# ActionChains(driver).drag_and_drop(source, target).perform()

#option 2
# ActionChains(driver) \
#     .click_and_hold(source) \
#     .move_to_element(target) \
#     .pause(0.5) \
#     .release() \
#     .perform()

#option 3
# driver.execute_script("""
#     var src = arguments[0];
#     var tgt = arguments[1];
#     var dataTransfer = new DataTransfer();
#     src.dispatchEvent(new DragEvent('dragstart', {dataTransfer}));
#     tgt.dispatchEvent(new DragEvent('drop', {dataTransfer}));
#     src.dispatchEvent(new DragEvent('dragend', {dataTransfer}));
# """, source, target)

#verify
# ActionChains(driver).drag_and_drop(source, target).perform()

# # Esperar que el card aparezca en la nueva columna
# wait.until(EC.presence_of_element_located(
#     (By.CSS_SELECTOR, "#done-column .card[id='card-1']")
# ))