class Solution(object):
    def containsDuplicate(self, nums):
        mySet = set(nums)
        
        if len(mySet) != len(nums):
            return True
        
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        