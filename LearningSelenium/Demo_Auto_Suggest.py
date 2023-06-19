import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class DemoAutoSuggest():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//span[@class='demo-icon icon-hotels']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(2)
        elem=driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(elem)
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
        time.sleep(2)
        try:
            elem1 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
            print(elem1)
        except:
            print("Element not displayed")

        time.sleep(4)

getAutoSuggest=DemoAutoSuggest()
getAutoSuggest.locate()