import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from FB_Signup_POM import SignupPage


class TestSignup():
    def test_signup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.facebook.com/r.php?entry_point=login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.sup=SignupPage(self.driver)
        self.sup.setFirstname(firstname="Remote")
        self.sup.setSurname("Acessing")
        self.sup.setDateofbirth("23")
        self.sup.setMonthofbirth("Dec")
        self.sup.setYearofbirth("2000")
        self.sup.clickMale()
        self.sup.setEmailaddress("RemoteAcessing@email.com")
        self.sup.setNewpassword("RemoteAcess@123")
        self.sup.clickSignUp()
        error_message=self.sup.is_registration_error_displayed()
        assert error_message.is_displayed()
        assert "There was an error with your registration." in error_message.text
        self.driver.quit()
