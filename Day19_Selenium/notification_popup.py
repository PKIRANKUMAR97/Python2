from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
ops.add_experimental_option("detach",True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=ops)

driver.maximize_window()
driver.get("https://whatmylocation.com/")

driver.quit()