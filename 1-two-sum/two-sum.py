class Solution(object):
    def twoSum(self, nums, target):
        indices = {}

        for i in range (len(nums)):
            if(target - nums[i]) in indices:
                return [i, indices[target-nums[i]]]
            
            indices[nums[i]] = i


        