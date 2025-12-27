import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://www.flipkart.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[contains(text(),'Flight Bookings')]").click()

time.sleep(5)
# driver.close()

driver.quit()