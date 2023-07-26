import pytest
import time
from selenium.webdriver.common.by import By
from pages.launch_page import launchPage
from pages.search_results_page import searchFlightResult
from utilities.utils import utils


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def testSearchFlights(self):
        lp=launchPage(self.driver)
        # lp.departfrom("New Delhi")
        lp.enterDepartFromLocation("New Delhi")
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
        ut=utils()
        ut.assertListText(allstops,"1 Stop")

