class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        s1 = set(nums1)
        s2 = set(nums2)
        '''
        intersect = s1.intersection(s2)
        return list(intersect)
        '''

        if len(s1) > len(s2):
            return self.intersect(s2, s1)
        return self.intersect(s1, s2)

    def intersect(self, set1, set2):
        return [x for x in set1 if x in set2]
        

sol = Solution()

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(sol.intersection(nums1, nums2))