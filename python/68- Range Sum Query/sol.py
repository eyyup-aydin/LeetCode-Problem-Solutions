
class NumArray:
    def __init__(self, nums):
        if nums is not None:
            self.numSums = [0 for _ in range(len(nums) + 1)]
            sum = 0
            for i, num in enumerate(nums):
                sum += num
                self.numSums[i + 1] = sum
    
    def sumRange(self, i, j):
        if self.numSums is not None:
            return self.numSums[j + 1] - self.numSums[i]


# naive solution
'''
class NumArray:
    def __init__(self, nums):
        self.nums = nums
    
    def sumRange(self, i, j):
        if self.nums is not None:
            sliced = self.nums[i:j+1]
            return sum(sliced)
'''