from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service(r"C:\browserdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)  ## we are launching the browser

driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
driver.maximize_window()

## self
# text_va1=driver.find_element(By.XPATH,"//a[contains(text(),'Prakash Steelage')]/self::a").text
# print(text_va1)

## parent
# text_va1_par=driver.find_element(By.XPATH,"//a[contains(text(),'Prakash Steelage')]/parent::td").text
# print(text_va1_par)

## child
# text_va1_child=driver.find_elements(By.XPATH,"//a[contains(text(),'Prakash Steelage')]/ancestor::tr/child::td")
# print(len(text_va1_child))  ## 6

##ancestor
# text_va1_anc=driver.find_element(By.XPATH,"//a[contains(text(),'Prakash Steelage')]/ancestor::tr").text
# print(text_va1_anc)   ## Prakash Steelage B 4.15 4.98 + 20.00 Buy  |  Sell

##decendent

# des=driver.find_elements(By.XPATH,"//a[contains(text(),'Prakash Steelage')]/ancestor::tr/descendant::*")
# for i in des:
#     print(i.text)
# print(len(des))    ## 10

## following

# foll=driver.find_elements(By.XPATH,"//a[contains(text(),'Prakash Steelage')]/ancestor::tr/following::*")
# print(len(foll))    ## 1284

## following-siblimg
# foll_sib=driver.find_elements(By.XPATH,"//a[contains(text(),'Prakash Steelage')]/ancestor::tr/following-sibling::*")
# print(len(foll_sib)) ##98

##preceding
# precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'Prakash Steelage')]/ancestor::tr/preceding::*")
# print(len(precedings))  ## 205

## preceding-sibling
preceding_sib=driver.find_elements(By.XPATH,"//a[contains(text(),'Prakash Steelage')]/ancestor::tr/preceding-sibling::tr")
print(len(preceding_sib))  # 1



