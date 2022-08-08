import time
import os
from traceback import print_stack
#from base.basepage import getters

class seleniumdriver():

    def __init__(self,driver):
        self.driver=driver
        #self.bsclass = getters(driver)

    def screenshot(self,result):
        filename=result + "." + str(round(time.time() * 1000))+".png"
        directory="/Users/viveksrinivasan/PycharmProjects/pyframework/ss"
        directory="../screenshots/"
        destination=directory+filename
        currentdirectory=os.path.dirname(__file__)
        #file
        dir2=os.path.join(currentdirectory,destination)
        # folder
        dir3=os.path.join(currentdirectory,directory)
        try:
            if not os.path.exists(dir3):
                os.makedirs(dir3)
            self.driver.save_screenshot(dir2)
            print("SS has been taken")
        except NotADirectoryError:
            print("Please check the path/directory")
            print_stack()

    def gettitle(self):
        return self.driver.title







