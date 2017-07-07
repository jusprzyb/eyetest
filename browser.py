from selenium.webdriver import Firefox

driver = None

def get_driver():
    global driver
    if not driver:
        driver = Firefox()
        driver.implicitly_wait(5)
    return driver