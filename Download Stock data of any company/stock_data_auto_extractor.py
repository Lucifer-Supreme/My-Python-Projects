#this program will not work as yahoo finance requires subscription to download stack history data
#alternate solution under way

from selenium import webdriver
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://finance.yahoo.com/")
    return driver

def search_scrape(driver):
    driver.find_element(by="xpath",value="/html/body/div[2]/header/div/div/div/div[2]/div/div[1]/div[3]/form/input[1]").send_keys("APPL")

def main():
    driver = get_driver()
    stock_name = input("Enter the stock name you want to search :")
    search_scrape(driver=driver)

main()