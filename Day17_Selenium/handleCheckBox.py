import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
driver.maximize_window()

## select specific checkbox
# driver.find_element(By.XPATH,"//input[@type='checkbox' and @value='one']").click()

## select multiple checkboxes
mul_checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'id_checkbox')]")
print(len(mul_checkboxes)) # 3

# for i in range(len(mul_checkboxes)):
#     mul_checkboxes[i].click()


## select multiple checkboxes by choice

# for checkbox in mul_checkboxes:
#     boxname=checkbox.__getattribute__("id")
#     if boxname=='id_checkboxes_1' or boxname=='id_checkboxes_2':
#        checkbox.click()


### select first 2 checkboxes
# for i in range(len(mul_checkboxes)):
#     if i<2:
#         mul_checkboxes[i].click()
#         time.sleep(2)



### clearing all checkboxes
for checkbox in mul_checkboxes:
    if checkbox.is_selected():        ## if it is already selected , it will unselect i.e clear the entry because a clink indicated select or unselect based on present status of checkbox
      checkbox.click()
    time.sleep(1)


driver.quit()