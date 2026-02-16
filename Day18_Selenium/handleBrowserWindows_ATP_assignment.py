import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



service = Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
all_search_links=driver.find_elements(By.XPATH,"//div[@id='wikipedia-search-result-link']/a")
print(len(all_search_links))

for link in all_search_links:
    print(link.text)
    link.click()

windowIDs=driver.window_handles
for windowID in windowIDs:
    driver.switch_to.window(windowID)
    print(windowID,driver.current_url)
    print(driver.title)

driver.quit()
