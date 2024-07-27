class Solution(object):
    def findDuplicate(self, nums):
        head = nums[0]
        trail = nums[0]

        while True:
            trail = nums[trail]
            head = nums[nums[head]]
            if trail == head:
                break

        finder = nums[0]
        while finder != trail:
            finder = nums[finder]
            trail = nums[trail]

        return finder