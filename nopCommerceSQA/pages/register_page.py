from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from selenium.webdriver.support.select import Select


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
    def getFirstName(self):
        return self.wait_elements_clickable(By.XPATH,self.first_name)
    def getLastName(self):
        return self.wait_elements_clickable(By.XPATH,self.last_name)
    def getDOBday(self):
        return self.wait_element_located(By.XPATH,self.dob_day)
    def getDOBmonth(self):
        return self.wait_element_located(By.XPATH,self.dob_month)
    def getDOByear(self):
        return self.wait_element_located(By.XPATH,self.dob_year)
    def getEmail(self):
        return self.wait_elements_clickable(By.XPATH,self.email)
    def getCompanyName(self):
        return self.wait_elements_clickable(By.XPATH,self.company_name)
    def getNewsletter(self):
        return self.wait_elements_clickable(By.XPATH,self.newsletter)
    def getPassword(self):
        return self.wait_elements_clickable(By.XPATH,self.password)
    def getConfirmPassword(self):
        return self.wait_elements_clickable(By.XPATH,self.confirm_password)
    def getRegisterButton(self):
        return self.wait_elements_clickable(By.XPATH,self.register_button)

    def clickGenderRadioButton(self,genderValue):
        if genderValue=="Male":
            self.getMaleGender().click()
        elif genderValue=="Female":
            self.getFemaleGender().click()
        else:
            print("Invalid input")
    def enterFirstName(self,firstname):
        self.getFirstName().send_keys(firstname)
    def enterLastName(self,lastname):
        self.getLastName().send_keys(lastname)
    def selectBirthDay(self, day):
        DOBday = Select(self.getDOBday())
        DOBday.select_by_value(day)
    def selectBirthMonth(self, month):
        DOBmonth = Select(self.getDOBmonth())
        DOBmonth.select_by_value(month)
    def selectBirthYear(self, year):
        DOByear = Select(self.getDOByear())
        DOByear.select_by_value(year)
    def enterEmail(self,email):
        self.getEmail().send_keys(email)
    def enterCompanyName(self,companyname):
        self.getCompanyName().send_keys(companyname)
    def clickNewsletter(self,status):
        if status=="cheacked" and self.getNewsletter().is_selected()==False:
            self.getNewsletter().click()
        elif status=="cheacked" and self.getNewsletter().is_selected()==True:
            pass
        elif status=="uncheacked" and self.getNewsletter().is_selected()==True:
            self.getNewsletter().click()
        elif status=="uncheacked" and self.getNewsletter().is_selected()==False:
            pass
        else:
            print("Invalid input")
    def enterPassword(self,password):
        self.getPassword().send_keys(password)
    def enterConfirmPassword(self,confirmpassword):
        self.getConfirmPassword().send_keys(confirmpassword)
    def clickRegisterButton(self):
        self.getRegisterButton().click()
    def register(self,type,dobDay,dobMonth,dobYear,firstName,
                     lastName,companyName,dynamicEmail,password,confirmPassword,newsletter):
        self.clickGenderRadioButton(type)
        self.selectBirthDay(dobDay)
        self.selectBirthMonth(dobMonth)
        self.selectBirthYear(dobYear)
        self.enterFirstName(firstName)
        self.enterLastName(lastName)
        self.enterCompanyName(companyName)
        self.enterEmail(dynamicEmail)
        self.enterPassword(password)
        self.enterConfirmPassword(confirmPassword)
        self.clickNewsletter(newsletter)
        self.clickRegisterButton()
