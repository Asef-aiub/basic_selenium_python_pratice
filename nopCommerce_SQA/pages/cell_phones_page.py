from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class CellPhonePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    nokia_lumia="//h2[@class='product-title']//a[contains(text(),'Nokia Lumia 1020')]"
    def getNokiaLumia(self):
        return self.wait_elements_clickable(By.XPATH, self.nokia_lumia)
    def clickNokiaLumia(self):
        self.getNokiaLumia().click()

