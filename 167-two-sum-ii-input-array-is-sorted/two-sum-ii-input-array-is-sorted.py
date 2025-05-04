class Solution(object):
    def twoSum(self, numbers, target):
        n1, n2 = 0,1

        while numbers[n1] + numbers[n2] != target:
            result = numbers[n1] + numbers[n2]
            if(result < target):
                n1 +=1
                n2 += 1
            if(result > target):
                n1 -=1
        return [n1+1, n2+1]
        