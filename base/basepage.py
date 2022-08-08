from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ecexp
from selenium.common.exceptions import *
from base.seleniumdriver import seleniumdriver

class getters(seleniumdriver):
    def __init__(self, driver):
        super(getters,self).__init__(driver)
        self.driver = driver
    #Will decide type of locator and gives result
    def getbytype(self, locater_type):
        locater_type = locater_type.lower()
        if locater_type == "id":
            return By.ID
        elif locater_type == "xpath":
            return By.XPATH
        else:
            print("Invalid Locator type")
        return False
    #will get type of element and sento to driver

    def getelement(self, locater , locater_type="Xpath"):
        element= None
        try:
            locater_type=locater_type.lower()
            bytype=self.getbytype(locater_type)
            element=self.driver.find_element(bytype,locater)
            print("Elements found")
        except:
            print("Element not found")
        return element
    #
    def elementispresent(self, locator, locater_type="Xpath"):
        try:
            locater_type = locater_type.lower()
            bytype = self.getbytype(locater_type)
            element = self.driver.find_element(bytype, locater_type)
            if len(element) > 0:
               print("element found")
               return True
            else:
                print("element not found")
                return False
        except:
            print("no elements found ")
        return False

    def gettext(self, locator, locatortype="xpath"):
        elements=None
        try:
            if locator:
                elements=self.getelement(locator,locatortype)
            gtext=elements.text
            if len(gtext) == 0:
                gtext=elements.get_attribute("innerText")
            if len(gtext) != 0:
                print("Text is",gtext)

        except:
            print("Failed to get the element!")
            print_stack()
            gtext=None

        return gtext

    def sendkey(self, locator,sendkeys,locatortype="xpath"):
        elements = None
        try:
            if locator:
                elements = self.getelement(locator, locatortype)
            elements.send_keys(sendkeys)
            print("Keys sent succesfully")

        except:
               print("Failed to get Keys!")
               print_stack()

    def onclick(self,locator,locatortype="xpath"):
        elements = None
        try:
            if locator:
                elements = self.getelement(locator, locatortype)
            elements.click()
            print("was  able to click")

        except:
            print("cannot able to click")
            print_stack()

    def waits(self, locator,timeout=10, poll_frequency=3,locatortype="xpath",visiblityexp="element_to_be_clickable"):
        elements=None
        try:
            locatortype = locatortype.lower()
            bytype = self.getbytype(locatortype)
            waitingtime=WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            elements=waitingtime.until(ecexp.visiblityexp((bytype,locator)))
            print("Element is Visible")
        except:
            print("Element are not Visible")
        return elements







































