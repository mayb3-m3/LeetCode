class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        r, c = next((i, j) for i in range(8) for j in range(8) if board[i][j] == 'R')
        count = 0
        for (i, j) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = r + i, c + j
            while 0 <= x <= 7 and 0 <= y <= 7:
                if board[x][y] == 'p':
                    count += 1
                    break
                if board[x][y] == 'B':
                    break
                x, y = x + i, y + j
        return count
