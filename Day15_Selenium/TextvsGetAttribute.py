from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://admin-demo.nopcommerce.com/login")

email=driver.find_element(By.XPATH, "//input[@id='Email']")
email.clear()
email.send_keys("abc@gmail.com")
print(email.text)
print(email.get_attribute("data-val-regex"))  ## Wrong email

