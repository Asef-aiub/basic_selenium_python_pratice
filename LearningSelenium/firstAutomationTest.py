# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# # Set up the ChromeDriver service
# driver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
#
# # Start the WebDriver with the service
# driver = webdriver.Chrome(service=driver_service)
#
# # driver=webdriver.Chrome(executable_path="E:\\BrwoserDrivers\\chromedriver.exe")
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
# print(driver.title)
# driver.close()

x="""from selenium import webdriver"""
print(x)
print(x.replace("webdriver","webdriver.Chrome"))
print("webdriver" in x)
y=8799870
#print(y.find("9"))
z=str(y)
print(z.find("9"))
print(z.rfind("9"))
print(z.index("9"))
a="     abc def ghi jkl mno pqr stu vwx yz"
print(a.split(" ",3))
print(a.rsplit(" ",2))
print(a.strip())
b="abc, def, ghi, jkl, mno, pqr, stu, vwx, yz"
print(b[0:b.index(",")])