import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.bcci.tv/international/men/stats/test")

## scroll to particular element
raina=driver.find_element(By.XPATH,"//h6[normalize-space()='Suresh Raina']")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",raina)
time.sleep(5)
