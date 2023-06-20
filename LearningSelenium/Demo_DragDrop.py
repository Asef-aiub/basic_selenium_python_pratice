import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoDragDrop():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        dragelement=driver.find_element(By.XPATH,"//div[@id='draggable']")
        dropelement=driver.find_element(By.XPATH,"//div[@id='droppable']")
        ActionChains(driver).drag_and_drop_by_offset(dragelement,0,100).perform()
        time.sleep(3)
        ActionChains(driver).drag_and_drop(dragelement,dropelement).perform()
        time.sleep(3)

ddrop=DemoDragDrop()
ddrop.locate()