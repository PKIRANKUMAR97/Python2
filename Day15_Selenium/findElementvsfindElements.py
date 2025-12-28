from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
########### findElement ###########
## 1.locator matching with single webelement
# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("T shits")

## 2.locator matching with multiple webelements
# element=driver.find_element(By.XPATH,"//footer[@class='footer']//a")
# print(element.text)

# 3.element not available then it should throw NoSuchElement exception
# no_ele=driver.find_element(By.LINK_TEXT,"Log")
# print(no_ele.text)

#########   findElements   ################ always returns list collection
## 1.locator matching with single webelement
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))
# elements[0].send_keys("Tshirts")


## 2.locator matching with multiple webelements
# elements=driver.find_elements(By.XPATH,"//footer[@class='footer']//a")
# print(len(elements))
# for element in elements:
#     print(element.text)


## 3. element not available: no exception will be thrown
no_ele=driver.find_elements(By.LINK_TEXT,"Log")
print(len(no_ele))
