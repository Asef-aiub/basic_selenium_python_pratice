import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver = driver
    def pageScroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(3)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == pageLength:
                match = True

        time.sleep(3)
    def wait_presence_element_located(self,loacator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        listofelements= wait.until(EC.presence_of_all_elements_located((loacator_type,locator)))
        return listofelements
    def wait_elements_clickable(self,loacator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        element= wait.until(EC.element_to_be_clickable((loacator_type,locator)))
        return element

    def wait_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element