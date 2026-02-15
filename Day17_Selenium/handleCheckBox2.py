from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

all_checkboxes=driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@id,'day')]")
# for i in range(len(all_checkboxes)):
#     all_checkboxes[i].click()

for checkbox in all_checkboxes:
    checkbox.click()

