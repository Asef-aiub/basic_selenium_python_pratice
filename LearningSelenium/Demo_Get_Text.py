import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoGetText():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        text=driver.find_element(By.XPATH,"//div[normalize-space()='Chennai']").text
        print(text)
        time.sleep(4)

getText=DemoGetText()
getText.locate()