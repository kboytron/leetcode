class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()

        input = ''.join(char for char in s if char.isalnum())

        i , j = 0, len(input) -1
        while i < j:
            if input[i] != input[j]:
                return False
            i+=1
            j-=1

       
        return True
        