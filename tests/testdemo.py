import unittest
from tests.login.selectedproject import searchproduct as sp
from tests.selectedproduct.selectedproject import searchproduct

tc1=unittest.TestLoader().loadTestsFromTestCase(sp)
tc2=unittest.TestLoader().loadTestsFromTestCase(searchproduct)
demo=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(demo)















