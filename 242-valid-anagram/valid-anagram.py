class Solution(object):
    def isAnagram(self, s, t):
        sMap = {}
        tMap = {}

        for char in s:
            if char in sMap:
                sMap[char] += 1
            else:
                sMap[char] = 1

        for char in t:
            if char in tMap:
                tMap[char] += 1
            else:
                tMap[char] = 1
        return sMap == tMap
        