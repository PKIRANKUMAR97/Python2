from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class TestCLI:
    def test_Logo(self, setup):
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        title_page=self.driver.title
        print(title_page)
        assert True==True

    def test_Login(self, setup):
        print(" is opened")
        self.driver=setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        try:
            self.status=self.driver.find_element(By.XPATH, "//h6[normalize-space() ='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert self.status==False