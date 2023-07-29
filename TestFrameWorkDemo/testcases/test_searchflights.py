import pytest
import time
import softest
from pages.launch_page import launchPage
from pages.search_results_page import searchFlightResult
from utilities.utils import utils
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    @data(*utils().read_data_from_excel("E:\\Python-Selenium\\TestFrameWorkDemo\\testdata\\tdataexcel.xlsx","Sheet1"))
    # @data(*utils().read_data_from_csv("E:\\Python-Selenium\\TestFrameWorkDemo\\testdata\\tdatacsv.csv"))
    @unpack
    def testSearchFlights(self,going_from,going_to,depart_date,stops):
        lp=launchPage(self.driver)
        lp.searchFlights(going_from,going_to,depart_date)
        time.sleep(3)
        sf=searchFlightResult(self.driver)
        sf.filter_flights_by_stop(stops)
        allstops=sf.getSearchFlightResult()
        time.sleep(3)
        print("")
        print(len(allstops))
        ut=utils()
        ut.assertListText(allstops,stops)

