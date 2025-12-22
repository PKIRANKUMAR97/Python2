"""
Test Case
---------------
1.Open web browser ( chrome/ fire fox)
2.open url -- https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
3. provide username --  Admin
4.provide password  --  admin123
5. click on login
6. capture title of dashboard page (Actual  Title )
7. verify title of page :
8. close browser

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# serv_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")  ## when we create an object for service class , it expects the location of executable path and the same service object needs top be placed inside the driver class
# driver = webdriver.Chrome(service=serv_obj)
driver=webdriver.Chrome()  ## we can use this after placing the .exe file of any particular driver in the python location
driver.get("https://opensource-demo.orangehrmlive.com/")

# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
wait = WebDriverWait(driver, 10)

wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("admin123")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

actual_title=driver.title
exp_title = "OrangeHRM"
if actual_title == exp_title:
    print("Test Passed")
else:
    print("Test Failed")

driver.close()
