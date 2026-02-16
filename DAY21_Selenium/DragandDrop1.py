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

driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manager")
action=ActionChains(driver)
driver.implicitly_wait(10)

frame = mywait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))
)
driver.switch_to.frame(frame)

source=driver.find_element(By.XPATH,"//img[@alt='The peaks of High Tatras']")
target=driver.find_element(By.XPATH,"//div[@id='trash']")
time.sleep(5)
action.drag_and_drop(source,target).perform()
