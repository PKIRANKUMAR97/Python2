import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser
driver.implicitly_wait(10)    ## implicit wait

driver.get("https://www.google.com/")
driver.maximize_window()

search_ele=(driver.find_element(By.NAME, "q"))
search_ele.send_keys("Selenium")
search_ele.submit()      # clicking enter in keyboard

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()