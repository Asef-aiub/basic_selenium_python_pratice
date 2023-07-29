from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class OrderSuccessPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    seccess_msg="//strong[normalize-space()='Your order has been successfully processed!']"
    def getSuccessMsg(self):
        return self.wait_element_located(By.XPATH, self.seccess_msg)
    def getOrderSuccessMsgText(self):
        return self.getSuccessMsg().is_displayed()