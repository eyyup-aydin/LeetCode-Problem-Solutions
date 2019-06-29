class Solution(object):
    # taken from discussions... very clever.
    
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dict = {}
        for i in range(9):
            dict[i + 1] = 10**i * 9
        
        for x in dict:
            group = x * dict[x]
            if n > group:
                n -= group
            else:
                number = n // x
                index = n % x
                
                if index == 0:
                    number -= 1
                    index = x
                
                found_number = str(10**(x-1) + number)
                return found_number[index - 1]

sol = Solution()

print(sol.findNthDigit(10))
'''
print(sol.findNthDigit(500))

print(sol.findNthDigit(555))
print(sol.findNthDigit(600))
print(sol.findNthDigit(1000))
print(sol.findNthDigit(10000))
print(sol.findNthDigit(300000))
print(sol.findNthDigit(9999999))
'''

