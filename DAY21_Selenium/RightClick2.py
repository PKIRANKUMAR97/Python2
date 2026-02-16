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

ryt_clk_element=driver.find_element(By.XPATH,"//button[@id='rightclick']")

action=ActionChains(driver)
action.context_click(ryt_clk_element).perform()
driver.find_element(By.XPATH,"//div[@id='myDiv']//a[normalize-space()='Registration Form']").click()
time.sleep(3)

