class Solution(object):
    def twoSum(self, nums, target):
        numsMap = {}

        for index,val in enumerate(nums):
            complement = target-val
            if complement in numsMap:
                return (numsMap[complement], index)
            numsMap[val] = index