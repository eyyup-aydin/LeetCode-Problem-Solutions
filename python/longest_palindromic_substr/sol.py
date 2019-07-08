class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2:
            return s

        d = {}
        max_len = 0
        max_i = 0
        max_j = 0
        for i in range(l):
            for j in range(i, l):
                if self.is_palindrome(s, i, j, d) and max_len < j - i + 1:
                    max_len = j - i + 1
                    max_i = i
                    max_j = j
        
        return s[max_i:max_j+1]



    def is_palindrome(self, s, i, j, d):
        if (i, j) in d:
            return d[(i, j)]

        if j - i < 2:
            d[(i, j)] = s[i] == s[j]
            return d[(i, j)]
           
        before = self.is_palindrome(s, i + 1, j - 1, d)
        
        d[(i, j)] = before and (s[i] == s[j])
        return d[(i, j)]
        
