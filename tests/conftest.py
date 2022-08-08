import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    print("driver started")
    yield
    print("Driver ended")

@pytest.fixture(scope="class")
def onetimesetup(request,browser="chrome"): #we have not sent anyparamere
    url="https://www.amazon.com"
    if browser == "chrome":
       driver = webdriver.Chrome(executable_path='./Driver/chromedriver')
    else:
        print("not valid browser")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(url)
    request.cls.driver=driver
    yield driver
    driver.quit()









