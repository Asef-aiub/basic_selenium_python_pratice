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
        lp.searchFlights("New Delhi","New york","21/08/2023")
        time.sleep(3)
        sf=searchFlightResult(self.driver)
        sf.filter_flights_by_stop("1 Stop")
        allstops=sf.getSearchFlightResult()
        time.sleep(3)
        print("")
        print(len(allstops))
        ut=utils()
        ut.assertListText(allstops,"1 Stop")

