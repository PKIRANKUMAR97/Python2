import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://vinothqaacademy.com/mouse-event/")

source_element= driver.find_element(By.XPATH,"//div[@id='draggableElement']")
target_element= driver.find_element(By.XPATH,"//div[@id='droppableElement']")

action=ActionChains(driver)
action.drag_and_drop(source_element,target_element).perform()
time.sleep(5)