import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoAutoSuggest():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        dpart= driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        dpart.click()
        time.sleep(2)
        dpart.send_keys("New Delhi")
        time.sleep(2)
        dpart.send_keys(Keys.ENTER)
        time.sleep(2)
        arrival=driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        arrival.send_keys("New")
        time.sleep(4)
        search=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search))
        for i in search:
            print(i.text)
            if "New York (LGA)" in i.text:
                i.click()
                time.sleep(2)
                break

        driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']").click()
        time.sleep(2)
        dates=driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
        for date in dates:
            if date.get_attribute("data-date")=="23/06/2023":
                date.click()
                time.sleep(3)
                break
        time.sleep(2)

getAutoSuggest=DemoAutoSuggest()
getAutoSuggest.locate()