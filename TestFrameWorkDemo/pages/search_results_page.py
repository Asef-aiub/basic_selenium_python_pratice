import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class searchFlightResult(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
    def filterFlights(self):
        self.driver.find_element(By.XPATH,"//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
        time.sleep(3)

