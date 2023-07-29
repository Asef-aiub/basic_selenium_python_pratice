import time
import unittest

import pytest
from pages.account_page import AccountPage
from pages.add_to_cart_page import AddCartPage
from pages.billing_page import BillingPage
from pages.cell_phones_page import CellPhonePage
from pages.order_success_page import OrderSuccessPage
from pages.shopping_cart_page import ShoppingCartPage
from utilities.utils import utils
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestPlaceOrder(unittest.TestCase):
    @data(*utils().read_data_from_excel("E:\\Python-Selenium\\nopCommerce_SQA\\testdata\\tdataexcel.xlsx","Billing"))
    @unpack
    def testPlaceOrder(self, firstname, lastname, email, country, city, address, zipcode, phone):
        ap=AccountPage(self.driver)
        ap.mouseHoverOnElectronicsAndClickCellPhone()
        cpp=CellPhonePage(self.driver)
        cpp.clickNokiaLumia()
        acp=AddCartPage(self.driver)
        acp.addToCart(2)
        scp=ShoppingCartPage(self.driver)
        scp.clickTearmsCheckboxAndCheckOutButton()
        scp.clickCheckoutAsGuestButton()
        bp=BillingPage(self.driver)
        bp.enterBillingAddress(firstname, lastname, email, country, city, address, zipcode, phone)
        bp.enterShippingMethod()
        bp.enterPaymentMethod()
        bp.enterPaymentInformation("Visa", "Michele Gerlach", "4693-9238-1753-7274", "09", "2025", "123")
        osp=OrderSuccessPage(self.driver)
        print(osp.getOrderSuccessMsgText())
        time.sleep(3)
