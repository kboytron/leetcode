class Solution(object):
    def twoSum(self, numbers, target):
        leftptr = 0
        rightptr = len(numbers)-1

        while leftptr < rightptr:
            if(numbers[leftptr] + numbers[rightptr] == target):
                return[leftptr+1,rightptr+1]
            
            if(numbers[leftptr] + numbers[rightptr] < target):
                leftptr+=1
            if(numbers[leftptr] + numbers[rightptr] > target):
                rightptr-=1
            