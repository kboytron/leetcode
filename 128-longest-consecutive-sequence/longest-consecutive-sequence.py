class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        max = 0

        for num in numSet:
            if num -1 not in numSet:
                count = 1
                curr = num
            
                while curr +1 in numSet:
                    count += 1
                    curr += 1

                if(count > max):
                    max = count
        return max
        