class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        count, n = 0, len(grid)
        for i in range(n):
            count += max(grid[i])
        for i in range(n):
            mx = 0
            for j in range(n):
                if grid[j][i] > 0:
                    count += 1
                mx = max(mx, grid[j][i])
            count += mx
        return count
