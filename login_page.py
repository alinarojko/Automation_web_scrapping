import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys


def get_driver():
    # Set option to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")        # disable infobars
    options.add_argument("start-maximazid")         # open browser in max size
    options.add_argument("disable-dev-shm-usage")   # to avoid issues with linux
    options.add_argument("no-sandbox")              # disable sandboxes
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")  # to avoid detection of the browsers

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def login():
    driver = get_driver()
    driver.find_element(By.ID, "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(By.ID, "id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class='navbar-brand']").click()
    print(driver.current_url)


print(login())

