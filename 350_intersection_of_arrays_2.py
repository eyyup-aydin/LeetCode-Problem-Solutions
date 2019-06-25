class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        dict1 = self.getDict(nums1)
        dict2 = self.getDict(nums2)
        result = []

        for k, v in dict1.items():
            if dict2.has_key(k):
                for i in range(min(v, dict2[k])):
                    result.append(k)

        return result
    
    def getDict(self, arr):
        '''
            actually python has this:
            c1 = collections.Counter(arr)
        '''
        dictionary = {}
        for num in arr:
            c = 1
            if dictionary.has_key(num):
                c += dictionary[num]
            dictionary[num] = c
        
        return dictionary


sol = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]

print(sol.intersect(nums1, nums2))







'''
neat solution:

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    c1 = collections.Counter(nums1)
    c2 = collections.Counter(nums2)
    
    res = []
    for k in list(set(c1.keys()) & set(c2.keys())):
        for _ in range(min(c1[k], c2[k])):
            res.append(k)
    return res

'''