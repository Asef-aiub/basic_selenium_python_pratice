import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoSS():
    def ss(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        continueButton=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        continueButton.screenshot(".\\test.png")
        continueButton.click()
        time.sleep(3)
        driver.get_screenshot_as_file(".\\test1.png")
        time.sleep(3)
ssdemo=DemoSS()
ssdemo.ss()