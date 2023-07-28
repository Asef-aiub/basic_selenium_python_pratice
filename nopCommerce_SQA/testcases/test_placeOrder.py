import time
import pytest

from pages.account_page import AccountPage
from pages.add_to_cart_page import AddCartPage
from pages.billing_page import BillingPage
from pages.cell_phones_page import CellPhonePage
from pages.shopping_cart_page import ShoppingCartPage
from utilities.utils import utils
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestPlaceOrder:
    @data(*utils().read_data_from_excel("E:\\Python-Selenium\\nopCommerce_SQA\\testdata\\registration_data.xlsx","Sheet2"))
    @unpack
    def testRegister(self,firstname,lastname,email,country,city,address,zip,phone):
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
        bp.enterBillingAddress()
        time.sleep(3)

        # rp=RegisterPage(self.driver)
        # rp.register(type,str(dobDay),str(dobMonth),str(dobYear),firstName,lastName,companyName,dynamicEmail,password,confirmPassword,newsletter)
        # rsp=RegSuccessPage(self.driver)
        # sm=rsp.getSuccessMsgText()
        # ut=utils()
        # ut.assertText(sm,"Your registration completed")
        # time.sleep(10)
