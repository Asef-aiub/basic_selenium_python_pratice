import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.launch_page import launchPage
from pages.search_results_page import searchFlightResult


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def testSearchFlights(self):
        lp=launchPage(self.driver)
        lp.departfrom("New Delhi")
        lp.destination("New York")
        lp.departuredate("21/08/2023")
        lp.search()
        time.sleep(3)
        sf=searchFlightResult(self.driver)
        sf.filterFlights()
        allstops=sf.wait_presence_element_located(By.XPATH,"//span[contains(text(),'Non Stop') or contains(text(),'1 Stop')]")
        time.sleep(3)
        print("")
        print(len(allstops))

        for stop in allstops:
            print(stop.text)
            assert stop.text=="1 Stop"
            print("assert pass")