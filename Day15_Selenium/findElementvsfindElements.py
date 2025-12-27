from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
########### findElement ###########
## locator matching with single webelement
# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("T shits")

## locator matching with multiple webelements
# element=driver.find_element(By.XPATH,"//footer[@class='footer']//a")
# print(element.text)

# element not available then it should throw NoSuchElement exception
no_ele=driver.find_element(By.LINK_TEXT,"Log")
print(no_ele.text)



