class Solution(object):
    def topKFrequent(self, nums, k):
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] +=1
            else:
                counts[num] = 1

        sortedCounts = sorted(counts.items(),key=lambda item: item[1], reverse=True)

        return [item[0] for item in sortedCounts[:k]]

        