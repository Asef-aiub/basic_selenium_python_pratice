import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoMultiWin():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.XPATH,"//a[@title='Yatra PRIME']//img[@class='conta iner']").click()
        time.sleep(2)
        currentwindow=driver.current_window_handle
        print(currentwindow)
        allwindows=driver.window_handles
        for window in allwindows:
            if window != currentwindow:
                driver.switch_to.window(window)
                time.sleep(4)
                print(window)
                driver.find_element(By.XPATH,"//a[@title='https://www.yatra.com']//i[@class='ico-newHeaderLogo']").click()
                time.sleep(2)
                driver.close()
                time.sleep(2)
                break
        driver.switch_to.window(currentwindow)
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
        time.sleep(4)
windowmanage=DemoMultiWin()
windowmanage.locate()