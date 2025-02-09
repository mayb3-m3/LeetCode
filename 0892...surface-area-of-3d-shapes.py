class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    area += 2
                for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= r < n and 0 <= c < n:
                        area += max(0, grid[i][j] - grid[r][c])
                    else:
                        area += grid[i][j]
        return area
