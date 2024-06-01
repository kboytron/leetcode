class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)

        result = 0

        for num in nums:
            if num -1 not in numSet: # if start of sequence
                current = num
                currResult = 1
            
                while current +1 in numSet:
                    current +=1
                    currResult +=1
                

                result = max(result,currResult)


        return result



        