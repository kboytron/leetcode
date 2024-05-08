class Solution(object):
    def twoSum(self, nums, target):
        result = [0,0]

        numsMap = {}

        for index,val in enumerate(nums):
            complement = target-val
            if complement in numsMap:
                return (numsMap[complement], index)
            numsMap[val] = index
        # return result