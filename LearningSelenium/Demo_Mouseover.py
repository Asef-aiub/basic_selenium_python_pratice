import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        #right click
        #achains.context_click(morebutton).perform()
        #double click
        #achains.double_click(morebutton).perform()
        # time.sleep(3)
        wait=WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Adventures']")))
        driver.find_element(By.XPATH,"//span[normalize-space()='Adventures']").click()
        time.sleep(3)
dmover=DemoMouseOver()
dmover.locate()