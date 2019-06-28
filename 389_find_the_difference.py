from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        counter = Counter(s + t)
        for char in counter:
            if counter[char] % 2 != 0:
                return char
        
        return ""

sol = Solution()
print(sol.findTheDifference("abced", "abiecd"))