class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n, count = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(1, m):
                if grid[j][i] <= grid[j-1][i]:
                    count += grid[j-1][i]+1 - grid[j][i]
                    grid[j][i] = grid[j-1][i] + 1
        return count
