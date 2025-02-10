class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        ans, n = True, len(grid)
        for i in range(n):
            for j in range(n):
                if (i == j or n-i-1 == j):
                    if grid[i][j] == 0:
                        ans = False
                        break 
                else:
                    if grid[i][j] != 0:
                        ans = False
                        break
        return ans
