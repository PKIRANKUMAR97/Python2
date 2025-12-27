from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

##is_displayed()
searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Displayed Status : " ,searchbox.is_displayed())


##is_enabled()
print("Enabled Status : " ,searchbox.is_enabled())

##is_selected()
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()

print("------After Selecting male radio button ------")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_female.click()
print("------After Selecting female radio button ------")
print(rd_male.is_selected())
print(rd_female.is_selected())





