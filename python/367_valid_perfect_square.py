class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = num ** 0.5    # exponent (power)
        return res == int(res)


sol = Solution()
print(sol.isPerfectSquare(16))
print(sol.isPerfectSquare(14))