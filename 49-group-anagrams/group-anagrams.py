class Solution(object):
    def groupAnagrams(self, strs):
        validAnagrams = {}
        for word in strs:
            sortedWord = tuple(sorted(word))

            if sortedWord in validAnagrams:
                validAnagrams[sortedWord].append(word)
            else:
                validAnagrams[sortedWord] = [word]

        return list(validAnagrams.values())
        