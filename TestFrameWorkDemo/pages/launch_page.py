import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver


class launchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    depart_from = "//input[@id='BE_flight_origin_city']"
    destination = "//input[@id='BE_flight_arrival_city']"
    depart_date= "//input[@id='BE_flight_origin_date']"
    all_date_element="//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']"
    search_button="//input[@value='Search Flights']"
    def getDepartFrom(self):
        return self.wait_elements_clickable(By.XPATH, self.depart_from)
    def getDestination(self):
        return self.wait_elements_clickable(By.XPATH, self.destination)
    def getDepartDate(self):
        return self.wait_elements_clickable(By.XPATH, self.depart_date)
    def getAllDateElement(self):
        return self.wait_elements_clickable(By.XPATH, self.all_date_element)
    def getSearchButton(self):
        return self.wait_elements_clickable(By.XPATH, self.search_button)
    def enterDepartFromLocation(self,departlocation):
        self.getDepartFrom().click()
        self.getDepartFrom().send_keys(departlocation)
        self.getDepartFrom().send_keys(Keys.ENTER)
    def enterDestinationLocation(self,destinationlocation):
        self.getDestination().click()
        self.getDestination().send_keys(destinationlocation)
        self.getDestination().send_keys(Keys.ENTER)
    def enterDeparturedate(self, departdate):
        self.getDepartDate().click()
        alldates = self.getAllDateElement().find_elements(By.XPATH, self.all_date_element)
        for date in alldates:
            if date.get_attribute("data-date") == departdate:
                date.click()
                break
    def clickSearch(self):
        self.getSearchButton().click()
        time.sleep(3)

    def searchFlights(self,departlocation,destinationlocation,departdate):
        self.enterDepartFromLocation(departlocation)
        self.enterDestinationLocation(destinationlocation)
        self.enterDeparturedate(departdate)
        self.clickSearch()

    # def departfrom(self,departlocation):
    #     departfrom=self.wait_elements_clickable(By.XPATH,"//input[@id='BE_flight_origin_city']")
    #     departfrom.click()
    #     departfrom.send_keys(departlocation)
    #     departfrom.send_keys(Keys.ENTER)

    # def departuredate(self, departdate):
    #     self.wait_elements_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
    #     dates_element = self.wait_elements_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
    #     dates = dates_element.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
    #     for date in dates:
    #         if date.get_attribute("data-date") == departdate:
    #             date.click()
    #             break
