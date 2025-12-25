from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser
driver.get("http://www.automationpractice.pl/index.php")
driver.maximize_window()

##absolute xpath
# driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"/html/body/div[6]/header/div[2]/div[2]/form/button").click()

##relative xpath
##or
# driver.find_element(By.XPATH,"//*[@id='search_query_top' or @name='search_']").send_keys("T-shirts") ## using OR option in xpath
# driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()

##and
# driver.find_element(By.XPATH,"//*[@id='search_query_top' and @name='search_query']").send_keys("T-shirts") ## using AND option in xpath
# driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()

##contains()   ## starts-with()
# driver.find_element(By.XPATH,"//input[contains(@id,'search_query_top')]").send_keys("T-shirts") ## using OR option in xpath
# driver.find_element(By.XPATH,"//button[starts-with(@name,'submit')]").click()

##text() -- to identify the element based on inner text
driver.find_element(By.XPATH,"//a[text()='Blog']")

