import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class searchFlightResult(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    filter_by_1_stop="//p[@class='font-lightgrey bold'][normalize-space()='1']"
    filter_by_2_stop="//p[@class='font-lightgrey bold'][normalize-space()='2']"
    filter_by_non_stop="//p[@class='font-lightgrey bold'][normalize-space()='0']"
    search_flight_result="//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"

    def getFilterBy1Stop(self):
        return self.wait_elements_clickable(By.XPATH, self.filter_by_1_stop)
    def getFilterBy2Stop(self):
        return self.wait_elements_clickable(By.XPATH, self.filter_by_2_stop)
    def getFilterByNonStop(self):
        return self.wait_elements_clickable(By.XPATH, self.filter_by_non_stop)
    def getSearchFlightResult(self):
        return self.wait_presence_element_located(By.XPATH, self.search_flight_result)
    def filter_flights_by_stop(self,by_stop):
        if by_stop == "1 Stop":
            self.getFilterBy1Stop().click()
            print("1 Stop")
            time.sleep(3)
        elif by_stop == "2 Stop":
            self.getFilterBy2Stop().click()
            print("2 Stop")
            time.sleep(3)
        elif by_stop == "Non Stop":
            self.getFilterByNonStop().click()
            print("Non Stop")
            time.sleep(3)
        else:
            print("Invalid input")

    # def filterFlights(self):
    #     self.driver.find_element(By.XPATH,"//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
    #     time.sleep(3)

