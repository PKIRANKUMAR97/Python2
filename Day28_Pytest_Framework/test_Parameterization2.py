import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class TestClass:
    @pytest.mark.parametrize('user,pwd',
                             [('Admin','admin123'),
                              ('Kiran','admin123'),
                              ('Admin','Kiran123'),
                              ('Kiran','Kiran123')
                              ])
    def test_Login_HRM(self,user,pwd):

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        try:
            self.status=self.driver.find_element(By.XPATH, "//h6[normalize-space() ='Dashboard']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert self.status==False
