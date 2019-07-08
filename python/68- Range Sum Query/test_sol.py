import unittest
from sol import NumArray

class Test_TestSol(unittest.TestCase):
    my_list = range(0, 10)
    my_sol = NumArray(my_list)

    def test1(self):
        self.assertEqual(self.my_sol.sumRange(0, 3), 6)
    
    def test2(self):
        self.assertEqual(self.my_sol.sumRange(2, 4), 9)
