import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.launch_page import launchPage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def testSearchFlights(self):
        lp=launchPage(self.driver,self.wait)
        lp.departfrom("New Delhi")
        time.sleep(3)
        lp.destination("New York")
        time.sleep(3)
        lp.departuredate("21/08/2023")
        time.sleep(3)
        lp.search()
        time.sleep(3)
