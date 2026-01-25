import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# from Day29_PageObjectModel.LoginPageObjects import LoginPage
from .LoginPageObjects import LoginPage


class TestLogin:
    def test_Login(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.clickLogin()

        self.actual_title=self.driver.title
        assert self.actual_title=="Just a moment..."
        self.driver.close()
