from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class RegSuccessPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    seccess_msg="//div[@class='result']"
    def getSuccessMsg(self):
        return self.wait_elements_clickable(By.XPATH, self.seccess_msg)
    def getSuccessMsgText(self):
        return self.getSuccessMsg().text