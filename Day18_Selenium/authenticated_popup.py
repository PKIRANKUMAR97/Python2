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

# driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth") ##handling authenticated popups using bypassing
driver.maximize_window()
time.sleep(3)
