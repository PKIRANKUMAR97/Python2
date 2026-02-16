from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()
mywait=WebDriverWait(driver,10)
driver.get("https://www.amazon.in/")
driver.implicitly_wait(15)
fresh= driver.find_element(By.XPATH,"//span[normalize-space()='Fresh']")
fresh_meat=mywait.until(EC.element_to_be_clickable((By.XPATH,"//img[@alt='Amazon Fresh Meat']")))

act = ActionChains(driver)

act.move_to_element(fresh).move_to_element(fresh_meat).click().perform()


