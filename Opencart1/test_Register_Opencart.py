import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Register_POM import RegisterPage


class TestRegister():
    def testRegister(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://demo.opencart.com/en-gb?route=account/register")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.rp=RegisterPage(self.driver)

        self.rp.setFirstName("HANA")
        self.rp.setLastName("SAP")
        self.rp.setEmail("saphana@email.com")
        self.rp.setPassword("SAPHANA@123")
        self.rp.acceptToggle()
        self.rp.clickContinue()
        self.driver.maximize_window()
        self.actual_title_on_page=self.driver.title
        assert self.actual_title_on_page=="Just a moment..."
        self.driver.close()
