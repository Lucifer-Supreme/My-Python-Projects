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
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver
  
def main():
    driver = get_driver()
    driver.find_element(by="id",value="CustomerEmail").send_keys("jeeshudutta20@gmail.com")
    time.sleep(3)
    driver.find_element(by="id",value="CustomerPassword").send_keys("Titan@13243546")
    time.sleep(3)
    driver.find_element(by="xpath",value="/html/body/main/article/section/div/div[1]/form/button").click()
    time.sleep(3)

main()