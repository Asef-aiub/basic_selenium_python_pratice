import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoMouseOver():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(3)
        achains=ActionChains(driver)
        morebutton=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        achains.move_to_element(morebutton).perform()
        time.sleep(3)
        driver.find_element(By.XPATH,"//span[normalize-space()='Adventures']").click()
        time.sleep(3)
dmover=DemoMouseOver()
dmover.locate()