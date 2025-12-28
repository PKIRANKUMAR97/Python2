import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

# mywait = WebDriverWait(driver,10)     ## explicit wait declaration ## basix syntax
mywait = WebDriverWait(driver,10,ignored_exceptions=[Exception])


driver.get("https://duckduckgo.com/")
driver.maximize_window()

search_ele=(driver.find_element(By.NAME, "q"))
search_ele.send_keys("snapdeal")
search_ele.submit()      # clicking enter in keyboard

search_link=mywait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Snapdeal.com')]")))
search_link.click()

driver.quit()

