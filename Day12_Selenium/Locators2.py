from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()   ## maximize the browser window
available_sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(available_sliders)
print(len(available_sliders))  # 5

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links)) # 88