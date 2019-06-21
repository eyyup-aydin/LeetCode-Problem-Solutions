
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

import sys

class Solution(object):

    def isBadVersion(self, n):
        return True

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.inner(1, n)
        
    
    def inner(self, start, end):
        mid = start + (end - start) // 2
        if isBadVersion(mid):
            if (mid - 1) >= start:
                return min(mid, self.inner(start, mid - 1))
            return mid
        elif (mid + 1) <= end:
            return self.inner(mid + 1, end)
        else:
            return sys.maxsize
