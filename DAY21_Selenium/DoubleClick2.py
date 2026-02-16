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

dbl_clk_element=driver.find_element(By.XPATH,"//button[@id='dblclick']")

action=ActionChains(driver)
action.double_click(dbl_clk_element).perform()
time.sleep(5)