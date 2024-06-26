class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(curr, open, close, n, result):

            if len(curr) == 2*n:
                result.append(curr)
                return

            if open < n:
                backtrack(curr + "(", open +1, close, n, result)

            if close < open:
                backtrack(curr + ")", open, close +1, n, result)

        result = []
        backtrack("", 0, 0, n, result)
        return result
        