class Solution(object):
    def isValid(self, s):
        stack = []

        closing = {')': '(','}':'{',']':'['}

        for char in s:
            if char in closing:
                if not stack:
                    return False
                test = stack.pop()

                if closing[char] != test:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0