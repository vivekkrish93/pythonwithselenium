from base.basepage import getters

class product(getters):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    search_box='//input[@id="twotabsearchtextbox"]'
    enter_click='//input[@value="Go"]'
    sectest="//span[text()='HP v236w 64GB USB 2.0 Pen Drive']"

    def search(self,product):
        self.onclick(self.search_box)
        self.sendkey(self.search_box,product)

    def clk(self):
        self.onclick(self.enter_click)

    def search_products(self,product="test"):
        self.search(product)
        self.clk

    def verifyproduct(self):
        self.waits(self.sectest)
        result=self.elementispresent(self.sectest)
        return result









