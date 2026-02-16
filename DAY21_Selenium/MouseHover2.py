import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

my_account_button=driver.find_element(By.XPATH,"//span[normalize-space()='My Account']")
my_account_button.click()
register_btn=driver.find_element(By.XPATH,"//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Register']")

action=ActionChains(driver)
action.move_to_element(register_btn).click().perform()

time.sleep(5)

