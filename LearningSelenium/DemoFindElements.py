import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindElements():
    def locate(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        list_a=driver.find_elements(By.TAG_NAME,('a'))
        print(len(list_a))
        for i in list_a:
            print(i.text)
        time.sleep(4)

find=DemoFindElements()
find.locate()