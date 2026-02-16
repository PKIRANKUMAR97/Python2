import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC



service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()
mywait=WebDriverWait(driver,10)

driver.get("https://flagpedia.net/index")
## scroll down by  pixels
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print("number of pixels moved= " , value)

## scroll down page till a particular element
# flag=driver.find_element(By.XPATH,"//img[@alt='Flag of England']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# time.sleep(6)
# value=driver.execute_script("return window.pageYOffset;")
# print("number of pixels moved= " , value)

## scroll down page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)

## scroll up page till start

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)