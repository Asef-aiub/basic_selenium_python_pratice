from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from selenium.webdriver.support.select import Select


class BillingPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    firstName="//input[@id='BillingNewAddress_FirstName']"
    lastName="//input[@id='BillingNewAddress_LastName']"
    email="//input[@id='BillingNewAddress_Email']"
    country="//select[@id='BillingNewAddress_CountryId']"
    city="//input[@id='BillingNewAddress_City']"
    address_id="BillingNewAddress_Address1"
    zip="//input[@id='BillingNewAddress_ZipPostalCode']"
    phone="//input[@id='BillingNewAddress_PhoneNumber']"
    continue_button="//button[@onclick='Billing.save()']"
    def getFirstName(self):
        return self.wait_elements_clickable(By.XPATH,self.firstName)
    def getLastName(self):
        return self.wait_elements_clickable(By.XPATH,self.lastName)
    def getEmail(self):
        return self.wait_elements_clickable(By.XPATH,self.email)
    def getCountry(self):
        return self.wait_element_located(By.XPATH,self.country)
    def getCity(self):
        return self.wait_elements_clickable(By.XPATH,self.city)
    def getAddress(self):
        return self.wait_elements_clickable(By.ID,self.address_id)
    def getZip(self):
        return self.wait_elements_clickable(By.XPATH,self.zip)
    def getPhone(self):
        return self.wait_elements_clickable(By.XPATH,self.phone)
    def getContinueButton(self):
        return self.wait_elements_clickable(By.XPATH,self.continue_button)

    def enterFirstName(self,firstname):
        self.getFirstName().send_keys(firstname)
    def enterLastName(self,lastname):
        self.getLastName().send_keys(lastname)
    def enterEmail(self,email):
        self.getEmail().send_keys(email)
    def selectCountry(self,country):
        countryName=Select(self.getCountry())
        countryName.select_by_visible_text(country)
    def enterCity(self,city):
        self.getCity().send_keys(city)
    def enterAddress(self,address):
        self.getAddress().send_keys(address)
    def enterZip(self,zip):
        self.getZip().send_keys(zip)
    def enterPhone(self,phone):
        self.getPhone().send_keys(phone)
    def clickContinueButton(self):
        self.getContinueButton().click()
    def enterBillingAddress(self,firstname,lastname,email,country,city,address,zip,phone):
        self.enterFirstName(firstname)
        self.enterLastName(lastname)
        self.enterEmail(email)
        self.selectCountry(country)
        self.enterCity(city)
        self.enterAddress(address)
        self.enterZip(zip)
        self.enterPhone(phone)
        self.clickContinueButton()
