class Solution(object):

    ## this solution taken from discussions
    
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        print("a:" + str(a) + " b:" + str(b))

        FILTER_32BIT = 0xffffffff

        while b & FILTER_32BIT:
            a, b = a ^ b, (a & b) << 1
        # bit cutoff needed only when carry overflows. 
        # Otherwise use Python regular integer
        return a & FILTER_32BIT if b > FILTER_32BIT else a
    

sol = Solution()
print(sol.getSum(4, 9))
print(sol.getSum(-2, 3))

