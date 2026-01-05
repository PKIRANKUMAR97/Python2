import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser
mywait = WebDriverWait(driver,10,ignored_exceptions=[Exception])

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

##opens alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(3)

alertwindowopened_3=driver.switch_to.alert      ### switch to alert # object of alert box
print(alertwindowopened_3.text)

alertwindowopened_3.send_keys("Hellooo")   ## enter data on the alert

# alertwindowopened_3.accept()     ### closes the alert by clicking on OK button
alertwindowopened_3.dismiss()      ### closes the alert by clicking on cancel button



