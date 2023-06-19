import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoFindElementByLinkText():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT,'Yatra for Business').click()
        time.sleep(4)

findbylinktext=DemoFindElementByLinkText()
findbylinktext.locate()