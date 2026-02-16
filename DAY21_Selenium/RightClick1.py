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

driver.get("https://swisnl.github.io/jQuery-contextMenu/3.x/demo.html")
button = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
action=ActionChains(driver)
action.context_click(button).click().perform()
