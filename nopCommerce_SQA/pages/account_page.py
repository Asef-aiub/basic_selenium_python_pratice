from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class AccountPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    electronics="//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']"
    cell_phones="//ul[@class='top-menu notmobile']//a[normalize-space()='Cell phones']"
    def getElectronics(self):
        return self.wait_element_located(By.XPATH, self.electronics)
    def getCellPhones(self):
        return self.wait_elements_clickable(By.XPATH, self.cell_phones)
    def mouseHoverOnElectronicsAndClickCellPhone(self):
        achains=ActionChains(self.driver)
        achains.move_to_element(self.getElectronics()).perform()
        self.getCellPhones().click()

