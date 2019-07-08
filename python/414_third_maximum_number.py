class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1 = None
        max_2 = None
        max_3 = None

        for num in nums:            
            if not (num == max_1 or num == max_2 or num == max_3):
                if not max_1 or num > max_1:
                    max_2, max_3 = max_1, max_2
                    max_1 = num
                elif (not max_2 or num > max_2) and num < max_1:
                    max_2, max_3 = num, max_2
                elif (not max_3 or num > max_3) and (max_2 and num < max_2):
                    max_3 = num

        if max_3 != None:
            return max_3
        return max_1

sol = Solution()

print(sol.thirdMax([3, 2, 1]))
print(sol.thirdMax([1, 2]))
print(sol.thirdMax([2, 2, 3, 1]))

print(sol.thirdMax([3,3,4,3,4,3,0,3,3]))