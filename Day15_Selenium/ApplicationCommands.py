from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()