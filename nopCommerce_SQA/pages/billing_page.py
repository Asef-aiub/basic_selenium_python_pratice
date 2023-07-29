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

    nex_day_air="shippingoption_1"
    continue_button2="//button[@onclick='ShippingMethod.save()']"

    credit_card="paymentmethod_1"
    continue_button3="//button[@onclick='PaymentMethod.save()']"

    select_card_type="//select[@id='CreditCardType']"
    cardholder_name="//input[@id='CardholderName']"
    card_number="//input[@id='CardNumber']"
    select_expiration_month="//select[@id='ExpireMonth']"
    select_expiration_year="//select[@id='ExpireYear']"
    card_code="//input[@id='CardCode']"
    continue_button4="//button[@onclick='PaymentInfo.save()']"
    confirm_button="//button[normalize-space()='Confirm']"

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
    def getNextDayAir(self):
        return self.wait_elements_clickable(By.ID,self.nex_day_air)
    def getContinueButton2(self):
        return self.wait_elements_clickable(By.XPATH,self.continue_button2)
    def getCreditCard(self):
        return self.wait_elements_clickable(By.ID,self.credit_card)
    def getContinueButton3(self):
        return self.wait_elements_clickable(By.XPATH,self.continue_button3)
    def getSelectCardType(self):
        return self.wait_element_located(By.XPATH,self.select_card_type)
    def getCardHolderName(self):
        return self.wait_elements_clickable(By.XPATH,self.cardholder_name)
    def getCardNumber(self):
        return self.wait_elements_clickable(By.XPATH,self.card_number)
    def getSelectExpirationMonth(self):
        return self.wait_element_located(By.XPATH,self.select_expiration_month)
    def getSelectExpirationYear(self):
        return self.wait_element_located(By.XPATH,self.select_expiration_year)
    def getCardCode(self):
        return self.wait_elements_clickable(By.XPATH,self.card_code)
    def getContinueButton4(self):
        return self.wait_elements_clickable(By.XPATH,self.continue_button4)
    def getConfirmButton(self):
        return self.wait_elements_clickable(By.XPATH,self.confirm_button)



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
    def clickNextDayAir(self):
        self.getNextDayAir().click()
    def clickContinueButton2(self):
        self.getContinueButton2().click()
    def clickContinueButton3(self):
        self.getContinueButton3().click()
    def clickContinueButton4(self):
        self.getContinueButton4().click()


    def enterBillingAddress(self,firstname,lastname,email,country,city,address,zipcode,phone):
        self.enterFirstName(firstname)
        self.enterLastName(lastname)
        self.enterEmail(email)
        self.selectCountry(country)
        self.enterCity(city)
        self.enterAddress(address)
        self.enterZip(zipcode)
        self.enterPhone(phone)
        self.clickContinueButton()
    def enterShippingMethod(self):
        self.clickNextDayAir()
        self.clickContinueButton2()
    def enterPaymentMethod(self):
        self.getCreditCard().click()
        self.clickContinueButton3()
    def selectCardType(self,cardtype):
        cardType=Select(self.getSelectCardType())
        cardType.select_by_visible_text(cardtype)
    def enterCardHolderName(self,cardholdername):
        self.getCardHolderName().send_keys(cardholdername)
    def enterCardNumber(self,cardnumber):
        self.getCardNumber().send_keys(cardnumber)
    def selectExpirationMonth(self,expirationmonth):
        expirationMonth=Select(self.getSelectExpirationMonth())
        expirationMonth.select_by_visible_text(expirationmonth)
    def selectExpirationYear(self,expirationyear):
        expirationYear=Select(self.getSelectExpirationYear())
        expirationYear.select_by_visible_text(expirationyear)
    def enterCardCode(self,cardcode):
        self.getCardCode().send_keys(cardcode)
    def clickContinueButton4(self):
        self.getContinueButton4().click()
    def enterPaymentInformation(self,cardtype,cardholdername,cardnumber,expirationmonth,expirationyear,cardcode):
        self.selectCardType(cardtype)
        self.enterCardHolderName(cardholdername)
        self.enterCardNumber(cardnumber)
        self.selectExpirationMonth(expirationmonth)
        self.selectExpirationYear(expirationyear)
        self.enterCardCode(cardcode)
        self.clickContinueButton4()
        self.getConfirmButton().click()
