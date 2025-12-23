from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser
driver.get("https://www.facebook.com/")
driver.maximize_window()   ## maximize the browser window

## tag & ID

#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("zxcvb")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("zxcvb")  ## tag is optional

# tag & class name
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("wert@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("wert@gmail.com")  # tag is optional

# tag attribute

# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal-email]").send_keys("nmhioqweerrdnhxyn@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal-email]").send_keys("nmhioqweerrdnhxyn@gmail.com")   # tag is optional

# tag class attribute

# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("asdfghtrjlwpoks")

driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal-pass]").send_keys("asdfghtrjlwpoks")  ## tag is optional
