import time
from datetime import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

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
    driver.get("http://automated.pythonanywhere.com")
    return driver


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def save_value_to_file(text):
    """Write input text into a file"""
    filename = f"{dt.now().strftime("%Y-%m-%d.%H-%M-%S")}.txt"
    with open(filename, "w") as file:
        file.write(text)


def main():
    driver = get_driver()
    while True:
        time.sleep(2)
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        save_value_to_file(text)


print(main())



