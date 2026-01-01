import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser
mywait = WebDriverWait(driver,20,ignored_exceptions=[Exception])


driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
drp_country_element=mywait.until(EC.presence_of_element_located((By.XPATH,"//select[@id='input-country']")))

# drp_country_object=Select(drp_country_element)
#
# # select option from dropdown
# drp_country_object.select_by_visible_text("India")
# # drp_country_object.select_by_value("1")
# # drp_country_object.select_by_index(4)   # index number counted from 0
#
#

