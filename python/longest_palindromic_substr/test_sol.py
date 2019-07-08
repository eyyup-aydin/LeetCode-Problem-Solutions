import unittest
from python.longest_palindromic_substr import sol

class Test_TestSolution(unittest.TestCase):
    sol = sol.Solution()

    def test1(self):
        res = self.sol.longestPalindrome("babad")
        ll = ["bab", "aba"]
        self.assertIn(res, ll)

    def test2(self):
        res = self.sol.longestPalindrome("cbbd")
        self.assertEqual(res, "bb")
    
    def test3(self):
        res = self.sol.longestPalindrome("")
        self.assertEqual(res, "")
    
    def test4(self):
        res = self.sol.longestPalindrome("ac")
        self.assertEqual(res, "a")

    def test5(self):
        res = self.sol.longestPalindrome("aaabaaaa")
        self.assertEqual(res, "aaabaaa")

if __name__ == '__main__':
    unittest.main()