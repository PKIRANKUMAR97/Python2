"""
https://www.naukri.com/nlogin/login?URL=https://www.naukri.com/mnjuser/homepage


"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/nlogin/login?URL=https://www.naukri.com/mnjuser/homepage")
driver.find_element(By.ID,"usernameField").send_keys("")
driver.find_element(By.ID,"passwordField").send_keys("")
driver.find_element(By.CLASS_NAME,"blue-btn").click()


actual_title_on_webpage=driver.title

print(actual_title_on_webpage)
expected_title="Jobseeker's Login: Search the Best Jobs available in India & Abroad - Naukri.com"

if actual_title_on_webpage == expected_title:
    print("Test passed")
else:
    print("Test failed")
