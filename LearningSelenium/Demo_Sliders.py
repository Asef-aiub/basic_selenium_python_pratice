import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoSlider():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.startech.com.bd/component")
        driver.maximize_window()
        time.sleep(3)
        lhandle=driver.find_element(By.XPATH,"//div[@title='Lower Handle']")
        rhandle=driver.find_element(By.XPATH,"//div[@title='Upper Handle']")
        achains=ActionChains(driver)
        achains.drag_and_drop_by_offset(lhandle,20,0).perform()
        time.sleep(3)
        achains.click_and_hold(lhandle).pause(1).move_by_offset(20,0).release().perform()
        time.sleep(3)
        achains.drag_and_drop_by_offset(rhandle,-30,0).perform()
        time.sleep(3)

dslider=DemoSlider()
dslider.locate()