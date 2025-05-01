class Solution(object):
    def containsDuplicate(self, nums):
        cleaned = set(nums) 

        if len(cleaned) != len(nums):
            return True
        return False

        