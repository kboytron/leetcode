class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        leftProds = 1

        for i in range(n):
            result[i] = leftProds
            leftProds *= nums[i]

        rightProds = 1
        for i in range(n-1,-1,-1):
            result[i] *= rightProds
            rightProds *= nums[i]

        return result
        