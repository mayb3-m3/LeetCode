class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l].isnumeric(): 
                            if board[k][l] in check:
                                return False
                            check.add(board[k][l])
        for i in range(9):
            check = set()
            for j in range(9):
                if board[i][j].isnumeric(): 
                    if board[i][j] in check:
                        return False
                    check.add(board[i][j])
        for i in range(9):
            check = set()
            for j in range(9):
                if board[j][i].isnumeric(): 
                    if board[j][i] in check:
                        return False
                    check.add(board[j][i])
        return True
