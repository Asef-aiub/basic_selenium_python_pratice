from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    register_button="//a[@class='ico-register']"
    def getRegisterButton(self):
        return self.wait_elements_clickable(By.XPATH, self.register_button)
    def clickRegisterButton(self):
        self.getRegisterButton().click()