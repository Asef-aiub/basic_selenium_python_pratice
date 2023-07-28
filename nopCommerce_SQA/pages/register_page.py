from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class RegisterPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    gender_male="//input[@id='gender-male']"
    gender_female="//input[@id='gender-female']"
    first_name="//input[@id='FirstName']"
    last_name="//input[@id='LastName']"
    dob_day="//select[@name='DateOfBirthDay']"
    dob_month="//select[@name='DateOfBirthMonth']"
    dob_year="//select[@name='DateOfBirthYear']"
    email="//input[@id='Email']"
    company_name="//input[@id='Company']"
    newsletter="//input[@id='Newsletter']"
    password="//input[@id='Password']"
    confirm_password="//input[@id='ConfirmPassword']"
    register_button="//button[@id='register-button']"
    def getMaleGender(self):
        return self.wait_elements_clickable(By.XPATH,self.gender_male)
    def getFemaleGender(self):
        return self.wait_elements_clickable(By.XPATH,self.gender_female)
    def clickGenderRadioButton(self,genderValue):
        if genderValue=="Male":
            self.getMaleGender().click()
        elif genderValue=="Female":
            self.getFemaleGender().click()
        else:
            print("Invalid input")

