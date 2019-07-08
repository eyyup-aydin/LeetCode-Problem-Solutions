from collections import Counter, OrderedDict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0 or l == 1:
            return l
            
        counter = Counter(s)
        total = 0
        remain = 0

        for char in counter:
            count = counter[char]
            total += (count // 2) * 2
            if remain == 0 and count % 2 != 0:
                remain = 1
        
        return total + remain


sol = Solution()
print()
print(sol.longestPalindrome("aA"))
print()
print(sol.longestPalindrome("bb"))
print()
print(sol.longestPalindrome("aAA"))



'''

            print("ch: " + char + " divide: " + str(divide) + " remain: " + str(remain) + " total: " + str(total) + " total_remains: " + str(total_remains))

for char in counter:
            num = counter[char]
            if not num in num_map:
                num_map[num] = []
            
            num_map[num].append(char)
        
        num_map = OrderedDict(sorted(num_map.items()))


        '''