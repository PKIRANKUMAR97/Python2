import pytest
from selenium.webdriver.common.by import By


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


class TestLogin:
    def test_Login_Chrome(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        assert self.driver.title=="OrangeHRM"
        self.driver.quit()

    def test_Login_Edge(self):
        from selenium import webdriver
        from selenium.webdriver.edge.service import Service

        self.service = Service(r"C:\browserdrivers\edgedriver_win64\msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.service)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()

    def test_Login_Firefox(self):
        from selenium import webdriver
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.firefox.options import Options
        from webdriver_manager.firefox import GeckoDriverManager

        options = Options()
        options.binary_location = r"C:\Users\reach\AppData\Local\Mozilla Firefox\firefox.exe"
        # ↑ adjust path to what `where firefox` shows

        self.driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options
        )


        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.quit()



