class Solution(object):
    def isValidSudoku(self, board):
        colset = [set() for n in range(9)]
        rowset = [set() for n in range(9)]
        squareset = [set() for n in range (9)]

        for i in range(9):
            for j in range(9):

                curr = board[i][j]

                if curr != '.':
                    sqIndex = (i // 3) * 3 + (j // 3)

                    if curr in rowset[i] or curr in colset[j] or curr in squareset[sqIndex]:
                        return False
                    
                    rowset[i].add(curr)
                    colset[j].add(curr)
                    squareset[sqIndex].add(curr)
        return True
        