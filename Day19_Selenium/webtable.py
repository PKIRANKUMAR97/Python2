import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=ops)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
noofrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
noofcolumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th"))

print(noofrows,noofcolumns)

c=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[2]")
if c.text == "Mukesh":
    print("pass")
time.sleep(5)
for r in range(2,noofrows+1):
    for c in range(1,noofcolumns+1):
        data =driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end ='       ')
    print()
driver.close()