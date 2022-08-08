from base.basepage import getters
from traceback import print_stack

class teststatus(getters):

    def __init__(self,driver):
        super(teststatus,self).__init__(driver)
        self.resultslist = []

    def setresult(self, result, resultmsg):
        try:
            if result is not None:
                if result:
                    self.resultslist.append("pass")
                    print("verification success",resultmsg)
                else:
                    self.resultslist.append("Fail")
                    print("verification fialed", resultmsg)
                    self.screenshot(resultmsg)
            else:
                self.resultslist.append("Fail")
                print("verification fialed", resultmsg)
                self.screenshot(resultmsg)
        except:
            self.resultslist.append("Fail")
            print("expection")
            self.screenshot(resultmsg)
            print_stack()

    def mark(self,result, resultmsg):
        self.setresult(result,resultmsg)

    def markfinal(self,testcasename,result, resultmsg):
        self.setresult(result, resultmsg)
        if "Fail" in self.resultslist:
            print(testcasename,"Test failed")
            self.resultslist.clear()
            #assert True == False
        else:
            print(testcasename, "Test pass")
            self.resultslist.clear()
            #assert True == True








