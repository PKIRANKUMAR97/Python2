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

driver.get("https://www.globalsqa.com/demoSite/practice/slider/range.html")

min_slider=mywait.until(EC.presence_of_element_located((By.XPATH,"//span[1]")))
max_slider=mywait.until(EC.presence_of_element_located((By.XPATH,"//span[2]")))
print("before sliding")
print(min_slider.location,max_slider.location)

action=ActionChains(driver)
action.drag_and_drop_by_offset(min_slider,100,0).perform()
action.drag_and_drop_by_offset(max_slider,-200,0).perform()
print("after sliding")
print(min_slider.location,max_slider.location)