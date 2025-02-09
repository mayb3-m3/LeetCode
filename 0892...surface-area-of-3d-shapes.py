class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 2*n*n
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0: # this creates 
                    area -= 2       # a hole in 3d
                if i+1 == n:
                    area += grid[i][j]
                else:
                    area += max(0, grid[i][j] - grid[i+1][j])
                if i-1 == -1:
                    area += grid[i][j]
                else:
                    area += max(0, grid[i][j] - grid[i-1][j])
                if j+1 == n:
                    area += grid[i][j]
                else:
                    area += max(0, grid[i][j] - grid[i][j+1])
                if j-1 == -1:
                    area += grid[i][j]
                else:
                    area += max(0, grid[i][j] - grid[i][j-1])
        return area
