import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# This replaces your manual path and service setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.fixture(scope="module")    ## decorator ## we will write all prerequisites

def setup():
    print("Launching browse....") # executes once before every test method
    print("Opening browser....")
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
    print("Closing browser....") # executes once after every test method

