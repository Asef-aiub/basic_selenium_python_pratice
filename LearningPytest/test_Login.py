import pytest
# pytest LearningPytest\test_Login.py -vk log
#E:\Python-Selenium>pytest -v
#E:\Python-Selenium>pytest -v -s
#E:\Python-Selenium>pytest -v -s -k log
#E:\Python-Selenium>pytest -v -s -k "not log"
def testLogin():
    print("Login test")
def testLogout():
    print("Logout test")

# E:\Python-Selenium>pytest -vm web
@pytest.mark.web
def testLogRegister():
    print("LogRegister test")
def Register():
    print("Register test")

@pytest.mark.web
def testCalculation():
    assert 1+2==3
@pytest.mark.skip
def testSkip():
    print("Skip test")
@pytest.mark.xfail
def testXfail():
    assert 1+2==4