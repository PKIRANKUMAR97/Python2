from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)
month="June"
year="2027"
date="10"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr =driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if month == mon and year == yr :
        break
    else :
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()


##enter date
dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
for date in dates:
    if date.text == date:
        date.click()
        break






