# # # Leer
# # value = driver.execute_script("return window.localStorage.getItem('key')")

# # # Escribir
# # driver.execute_script("window.localStorage.setItem('key', 'value')")

# # # Borrar todo
# # driver.execute_script("window.localStorage.clear()")
# # driver.execute_script("window.sessionStorage.clear()")



# #subir archivos
# # Caso típico — input type="file"
# file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")

# # Send_keys con la ruta absoluta — NO uses click + dialog
# file_input.send_keys("/Users/borja/Desktop/test_image.png")




# #descargas
# # Configurar carpeta de descargas
# options = webdriver.ChromeOptions()
# prefs = {
#     "download.default_directory": "/Users/borja/Downloads/test",
#     "download.prompt_for_download": False
# }
# options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(options=options)

# # Trigger download
# driver.find_element(By.ID, "download-btn").click()

# # Esperar a que el archivo aparezca
# import os, time
# filepath = "/Users/borja/Downloads/test/report.pdf"
# timeout = 30
# while not os.path.exists(filepath) and timeout > 0:
#     time.sleep(1)
#     timeout -= 1

# assert os.path.exists(filepath)