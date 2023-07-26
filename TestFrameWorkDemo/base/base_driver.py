import time


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