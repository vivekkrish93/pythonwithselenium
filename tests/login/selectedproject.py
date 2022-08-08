from page.selectedproduct.selectedproject import product
from utilites.teststatus import teststatus
import pytest
import unittest

@pytest.mark.usefixtures("onetimesetup","setup")
class searchproduct(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectup(self,onetimesetup):#init construct
        self.callfun=product(self.driver)
        self.teststat=teststatus(self.driver)
    def test_3(self):
        self.callfun.search_products("pendrive")
        result=self.callfun.verifyproduct()
        self.teststat.mark(result,resultmsg="product verification")
        self.teststat.markfinal("testcase_1",result,"search the product")








