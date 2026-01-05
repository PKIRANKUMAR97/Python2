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
mywait = WebDriverWait(driver,10,ignored_exceptions=[Exception])

driver.get("https://www.facebook.com/r.php?entry_point=login")
driver.maximize_window()

# # select option from dropdown
# dropdown_month_element=mywait.until(EC.presence_of_element_located((By.XPATH,"//select[@id='month']")))
# dropdown_month_object=Select(dropdown_month_element)
# dropdown_month_object.select_by_visible_text("Feb")
# dropdown_month_object.select_by_value("8")
# dropdown_month_object.select_by_index(11)

## capture all the options and print them
# all_available_options=dropdown_month_object.options
# print(len(all_available_options))
# for option in all_available_options:
#     print(option.text)

## select option from dropdown without using builtin functions
# for option in all_available_options:
#     if option.text == "Nov":
#         option.click()


## without using select class
alloptions=driver.find_elements(By.XPATH,"//*[@id='month']/option")
print(len(alloptions))

time.sleep(3)