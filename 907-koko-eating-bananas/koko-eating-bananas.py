class Solution(object):
    def minEatingSpeed(self, piles, h):
        def speedCheck(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = (left+right) // 2

            if speedCheck(mid):
                right = mid
            else:
                left = mid + 1
        return left
        