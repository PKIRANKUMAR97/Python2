from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SignupPage:

    # Locators
    textbox_Firstname_XPATH="//input[@name='firstname' and @aria-label='First name']"
    textbox_Surname_XPATH="//input[@name='lastname' and @aria-label='Surname']"
    dropdown_dateofbirth_XPATH="//select[@aria-label='Day']"
    dropdown_monthofbirth_XPATH="//select[@aria-label='Month']"
    dropdown_yearofbirth_XPATH="//select[@aria-label='Year']"
    button_gender_female_XPATH="//label[normalize-space()='Female']"
    button_gender_male_XPATH="//label[normalize-space()='Male']"
    button_gender_other_XPATH="//label[normalize-space()='Custom']"
    textbox_Emailaddress_XPATH="//input[@name='reg_email__' and @aria-label='Mobile number or email address']"
    textbox_Newpassword_XPATH="//input[@id='password_step_input']"
    button_SignUp_XPATH="//button[@type='submit' and text()='Sign up']"
    registration_error_ID="reg_error_inner"

    # Constructors
    def __init__(self, driver):
        self.driver = driver
    # Action Methods
    def setFirstname(self, firstname):
        firstNametext=self.driver.find_element(By.XPATH,self.textbox_Firstname_XPATH)
        firstNametext.clear()
        firstNametext.send_keys(firstname)

    def setSurname(self, surname):
        surnametext=self.driver.find_element(By.XPATH,self.textbox_Surname_XPATH)
        surnametext.clear()
        surnametext.send_keys(surname)

    def setDateofbirth(self, dateofbirth):
        dateofbirthtext=self.driver.find_element(By.XPATH,self.dropdown_dateofbirth_XPATH)
        # dateofbirthtext.clear()
        dateofbirthtext.send_keys(dateofbirth)

    def setMonthofbirth(self, monthofbirth):
        monthofbirthtext=self.driver.find_element(By.XPATH,self.dropdown_monthofbirth_XPATH)
        # monthofbirthtext.clear()
        monthofbirthtext.send_keys(monthofbirth)

    def setYearofbirth(self, yearofbirth):
        yearofbirthtext=self.driver.find_element(By.XPATH,self.dropdown_yearofbirth_XPATH)
        # yearofbirthtext.clear()
        yearofbirthtext.send_keys(yearofbirth)

    def clickMale(self):
        self.driver.find_element(By.XPATH,self.button_gender_female_XPATH).click()

    def setEmailaddress(self, emailaddress):
        emailaddresstext=self.driver.find_element(By.XPATH,self.textbox_Emailaddress_XPATH)
        emailaddresstext.clear()
        emailaddresstext.send_keys(emailaddress)

    def setNewpassword(self, newpassword):
        newpasswordtext=self.driver.find_element(By.XPATH,self.textbox_Newpassword_XPATH)
        newpasswordtext.clear()
        newpasswordtext.send_keys(newpassword)

    def clickSignUp(self):
        self.driver.find_element(By.XPATH,self.button_SignUp_XPATH).click()



    def is_registration_error_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, self.registration_error_ID)
            )
        )

