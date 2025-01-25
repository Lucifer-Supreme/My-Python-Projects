from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service('C:\\Users\\jeesh\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    #extract only the temperature
    #output = float(text.split(": ")[1])
    #return output
    output = text.split(": ")
    return output[1]

def main():
    driver = get_driver()
    time.sleep(3)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

print(main())
    