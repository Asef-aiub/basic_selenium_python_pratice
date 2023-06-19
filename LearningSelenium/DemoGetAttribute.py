import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoGetAttribute():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        att_value=driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(att_value)
        time.sleep(4)

getAttribute=DemoGetAttribute()
getAttribute.locate()