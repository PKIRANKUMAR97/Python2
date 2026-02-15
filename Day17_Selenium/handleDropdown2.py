from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
drop_down_country_element=driver.find_element(By.ID, "country")
country=Select(drop_down_country_element)
# country.select_by_value("india")
# country.select_by_visible_text("Canada")
country.select_by_index(3)   ## index starts with 0
driver.implicitly_wait(5)
