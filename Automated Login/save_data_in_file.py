from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import datetime as dt
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
    driver.get("https://automated.pythonanywhere.com")
    return driver

def clean_text(element):
    temp = element.split(": ")
    return temp[1]

def scrapping(driver):
        time.sleep(4)
        element= driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
        return clean_text(element.text+"°C")

def write_file(data):
     filename = f"Automated Login\\{dt.datetime.now().strftime("%Y-%m-%d.%H-%M-%S")}.txt"
     with open(filename,'w') as file:
          file.write(data)

def main ():
    driver = get_driver()
    while 1==1:
        data = scrapping(driver=driver)
        write_file(data)
        print(data)
    
print(main())   
