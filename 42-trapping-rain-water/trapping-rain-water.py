class Solution(object):
    def trap(self, height):
        maxL,maxR, result = 0,0,0

        lptr = 0
        rptr = len(height) -1

        while(lptr <= rptr):
            if height[lptr] < height[rptr]:
                if height[lptr] > maxL:
                    maxL = height[lptr]
                else:
                    result += maxL - height[lptr]
                lptr += 1
            else:
                if height[rptr] > maxR:
                    maxR = height[rptr]
                else:
                    result += maxR-height[rptr]
                rptr -= 1           
        return result
        