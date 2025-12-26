from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser
driver.get("https://www.flipkart.com/")
driver.maximize_window()

## Relative xpath directly from the web page
# driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']").send_keys("Fridges")
# driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More']").click()


## Relative xpath with AND option
# driver.find_element(By.XPATH,"//input[@class='lNPl8b' and @placeholder='Search for Products, Brands and More']").send_keys("Mobile phones")
# driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More' and @type='submit']").click()

## Relative xpath with OR option
# driver.find_element(By.XPATH,"//input[@class='lNPl8b' or @placeholder='Search for Products, Brands and More']").send_keys("Mobile phones")
# driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More' or @type='submit']").click()

##contains()
# driver.find_element(By.XPATH,"//input[contains(@placeholder,'Search for Products,')]").send_keys("Mobile phones 5G")
# driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More' or @type='submit']").click()

## starts-with()
driver.find_element(By.XPATH,"//input[starts-with(@placeholder,'Sea')]").send_keys("Laptops")
driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More' or @type='submit']").click()


# //input[@placeholder='Search for Products, Brands and More']
# //button[@title='Search for Products, Brands and More']//*[name()='svg']