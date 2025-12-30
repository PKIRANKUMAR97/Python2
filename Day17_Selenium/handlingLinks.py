import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

## click on the link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()

## find number of links in a page
all_links=driver.find_elements(By.XPATH,"//a" )
print(len(all_links))

for link in all_links:
    print(link.text)