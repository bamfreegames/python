# # Obtener todas las cookies
# cookies = driver.get_cookies()
# # [{'name': 'session', 'value': 'abc123', 'domain': '...', ...}]

# # Obtener una específica
# session = driver.get_cookie("session")

# # Añadir una cookie (útil para saltarse login)
# driver.add_cookie({
#     "name": "session",
#     "value": "abc123",
#     "domain": ".crypto-finance.com"
# })

# # Borrar
# driver.delete_cookie("session")
# driver.delete_all_cookies()



#saltar login anadiendo cookie sesion
def test_dashboard(driver):
    # 1. Cargar primero la página (debes estar en el dominio para añadir cookies)
    driver.get("https://app.example.com")
    
    # 2. Añadir cookie de sesión válida
    driver.add_cookie({"name": "session_token", "value": "valid_token_here"})
    
    # 3. Refrescar — ahora estás logueado
    driver.refresh()
    
    # 4. Ya puedes ir a páginas autenticadas
    driver.get("https://app.example.com/dashboard")