class Solution(object):
    def minimumSum(self, num):
        digits = sorted(str(num))
        new1 = int(digits[0] + digits[3]) # make a pair of lowest and highest digit
        new2 = int(digits[1]+digits[2])
        
        
        return new1+new2
        """
        :type num: int
        :rtype: int
        """
        