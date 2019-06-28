from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        c = Counter(s)
        for index, char in enumerate(s):
            if c[char] == 1:
                return index
        
        return -1

sol = Solution()
print(sol.firstUniqChar("leetcode"))
print(sol.firstUniqChar("loveleetcode"))
print(sol.firstUniqChar("aabbccddd"))
