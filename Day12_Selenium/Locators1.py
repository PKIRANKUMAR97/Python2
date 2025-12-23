from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()   ## maximize the browser window
## ID, NAME
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")
#driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad Carbon Laptop")

## LINK TEXT , PARTIAL LINK TEXT
##driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

