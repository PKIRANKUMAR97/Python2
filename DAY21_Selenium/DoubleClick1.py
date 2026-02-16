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

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
action=ActionChains(driver)
driver.implicitly_wait(10)
driver.switch_to.frame("iframeResult")
b1= driver.find_element(By.ID,"field1")
b1.clear()
b1.send_keys("HELLOOOOOOOO")
driver.implicitly_wait(10)

res_button= driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

action.double_click(res_button).click().perform()