import pytest

# # Screenshot de toda la página
# driver.save_screenshot("screenshot.png")

# # Screenshot de un elemento específico
# element = driver.find_element(By.ID, "header")
# element.screenshot("header.png")

# # Como bytes (para CI/CD que sube artifacts)
# png_bytes = driver.get_screenshot_as_png()





#automatico
# conftest.py
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.failed and "driver" in item.fixturenames:
        driver = item.funcargs["driver"]
        screenshot_path = f"screenshots/{item.name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")