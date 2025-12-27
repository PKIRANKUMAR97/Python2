from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.get("https://www.amazon.com/")
time.sleep(2)

driver.back() # flipkart
time.sleep(2)

driver.forward()  # amazon
time.sleep(2)

driver.refresh()