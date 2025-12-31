import time

import requests
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME,"a")
broken_count= 0
for link in all_links:
    url=link.get_attribute("href")
    try:
        responseofurl=requests.head(url)
    except:
        None
    if responseofurl.status_code >=400:
        print(url," is a broken link")
        broken_count += 1
    else:
        print(url," is a valid link")

print("total number of broken links :" , broken_count)
