from page.selectedproduct.selectedproject import product
from utilites.teststatus import teststatus
import pytest
import unittest
from ddt import ddt,data,unpack
# from utilites.readdata import getcsvdata
from utilites.readdata import getxldata

@pytest.mark.usefixtures("onetimesetup","setup")
@ddt 
class searchproductbycsv(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectup(self,onetimesetup):#init construct
        self.callfun=product(self.driver)
        self.teststat=teststatus(self.driver)

    @data(*getxldata("/Users/viveksrinivasan/PycharmProjects/pyframework/data2.xls"))
    @unpack
    def test_2(self,productName,username):
        self.callfun.search_products(productName)
        print('Unme',username)
        result=self.callfun.verifyproduct()
        self.teststat.mark(result,resultmsg="product verification")
        self.teststat.markfinal("testcase_1",result,"search the product")








