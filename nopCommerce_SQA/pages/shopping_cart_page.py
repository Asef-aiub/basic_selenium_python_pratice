from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class ShoppingCartPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    tearms_checkbox="//input[@id='termsofservice']"
    checkout_button="(//button[normalize-space()='Checkout'])[1]"
    checkout_as_guest_button="//button[normalize-space()='Checkout as Guest']"
    def getTearmsCheckbox(self):
        return self.wait_elements_clickable(By.XPATH, self.tearms_checkbox)
    def getCheckoutButton(self):
        return self.wait_elements_clickable(By.XPATH, self.checkout_button)
    def getCheckoutAsGuestButton(self):
        return self.wait_elements_clickable(By.XPATH, self.checkout_as_guest_button)
    def clickTearmsCheckboxAndCheckOutButton(self):
        self.getTearmsCheckbox().click()
        self.getCheckoutButton().click()
    def clickCheckoutAsGuestButton(self):
        self.getCheckoutAsGuestButton().click()


