import time
import pytest
from pages.home_page import HomePage
from pages.reg_success_page import RegSuccessPage
from pages.register_page import RegisterPage
from ddt import ddt, data, unpack
from utilities.utils import utils


@pytest.mark.usefixtures("setup")
@ddt
class TestRegistration():
    # @data(*utils().read_data_from_excel("E:\\Python-Selenium\\nopCommerce_SQA\\testdata\\tdataexcel.xlsx","Sheet1"))
    @data(*utils().read_data_from_csv("E:\\Python-Selenium\\nopCommerceSQA\\testdata\\tdata.csv"))
    @unpack

    def testRegister(self,type,dobDay,dobMonth,dobYear,firstName,
                     lastName,companyName,dynamicEmail,password,confirmPassword,newsletter):
        hp= HomePage(self.driver)
        rp = RegisterPage(self.driver)
        rsp = RegSuccessPage(self.driver)
        ut = utils()

        hp.clickRegisterButton()
        time.sleep(3)
        rp.register(type,str(dobDay),str(dobMonth),str(dobYear),
                    firstName,lastName,companyName,dynamicEmail,password,confirmPassword,newsletter)
        sm=rsp.getSuccessMsgText()
        ut.assertText(sm,"Your registration completed")
        time.sleep(5)
