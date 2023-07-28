import time

import pytest
import softest

from pages.home_page import HomePage
from pages.register_page import RegisterPage


@pytest.mark.usefixtures("setup")
class TestRegistration(softest.TestCase):
    def testRegister(self):
        hp= HomePage(self.driver)
        hp.clickRegisterButton()
        time.sleep(3)
        rp=RegisterPage(self.driver)
        rp.clickGenderRadioButton("Male")
        time.sleep(3)
