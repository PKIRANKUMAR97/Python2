from selenium import webdriver
from selenium.webdriver.common.by import By


class RegisterPage:
    # Locators
    textbox_FirstName_XPATH="//input[@input-firstname]"
    textbox_LastName_XPATH="//input[@id='input-lastname']"
    textbox_Email_XPATH="//input[@id='input-email']"
    textbox_password_XPATH="//input[@id='input-password']"
    button_accept_XPATH="//input[@name='agree']"
    button_Continue_XPATH="//button[normalize-space()='Continue']"

    # Constructors
    def __init__(self,driver):
        self.driver=driver

    # Action methods
    def setFirstName(self,firstname):
        firstNametxt=self.driver.find_element(By.ID,self.textbox_FirstName_XPATH)
        firstNametxt.clear()
        firstNametxt.send_keys(firstname)

    def setLastName(self,lastname):
        lastNametxt=self.driver.find_element(By.XPATH,self.textbox_LastName_XPATH)
        lastNametxt.clear()
        lastNametxt.send_keys(lastname)

    def setEmail(self,email):
        emailtxt=self.driver.find_element(By.XPATH,self.textbox_Email_XPATH)
        emailtxt.clear()
        emailtxt.send_keys(email)

    def setPassword(self,password):
        passwordtxt=self.driver.find_element(By.XPATH,self.textbox_password_XPATH)
        passwordtxt.clear()
        passwordtxt.send_keys(password)

    def acceptToggle(self):
        self.driver.find_element(By.XPATH,self.button_accept_XPATH).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.button_Continue_XPATH).click()



