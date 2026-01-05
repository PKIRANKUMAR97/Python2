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

driver.get("https://www.rediffmailpro.com/cgi-bin/login.cgi")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@type='submit']").click()

login_alert=driver.switch_to.alert
print(login_alert.text)
login_alert.accept()