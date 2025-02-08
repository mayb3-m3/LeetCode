class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col, count = len(grid), len(grid[0]), 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if i+1 == row or grid[i+1][j] == 0:
                        count += 1
                    if i-1 == -1 or grid[i-1][j] == 0:
                        count += 1
                    if j+1 == col or grid[i][j+1] == 0:
                        count += 1
                    if j-1 == -1 or grid[i][j-1] == 0:
                        count += 1
        return count
