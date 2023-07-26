import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver


class launchPage(BaseDriver):
    def __init__(self, driver,wait):
        self.driver = driver
        self.wait = wait
    def departfrom(self,departlocation):
        departfrom=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_city']")))
        departfrom.click()
        departfrom.send_keys(departlocation)
        departfrom.send_keys(Keys.ENTER)
    def destination(self,destinationlocation):
        destination=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_arrival_city']")))
        destination.click()
        destination.send_keys(destinationlocation)
        #search_results=self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='viewport']//div[1]/li")))
        destination.send_keys(Keys.ENTER)
    def departuredate(self, departdate):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        dates_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']"))
        )
        dates = dates_element.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
        for date in dates:
            if date.get_attribute("data-date") == departdate:
                date.click()
                break

    def search(self):
        search=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@value='Search Flights']")))
        search.click()
        time.sleep(3)