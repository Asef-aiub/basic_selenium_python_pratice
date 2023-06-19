import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoState():
    def state(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        d_state=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(d_state)
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("abcd")
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("abcd")
        d_state1=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(d_state1)
        time.sleep(4)

findDemoState=DemoState()
findDemoState.state()
