import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from selenium.webdriver.chrome.options import Options

ops = Options()
ops.add_experimental_option("detach", True)

# Pass 'options' to the driver

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=ops)
driver.maximize_window()
mywait=WebDriverWait(driver,10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.current_url)
print(driver.title)
page2=mywait.until(EC.element_to_be_clickable((By.LINK_TEXT,"OrangeHRM, Inc")))
page2.click()
time.sleep(3)
windowIDs = driver.window_handles

parentwindowid=windowIDs[0]
childwindowid=windowIDs[1]

driver.switch_to.window(childwindowid)
print(driver.current_url)
print(driver.title)
driver.close()

