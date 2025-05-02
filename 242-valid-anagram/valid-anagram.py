class Solution(object):
    def isAnagram(self, s, t):
        check = {}
        if(len(s) != len(t)):
            return False
        for char in s:
            if char in check:
                check[char] += 1
            else:
                check[char] = 1
        
        for char in t:
            if char not in check or check[char] == 0:
                return False
            check[char] -= 1
        return True
    
        