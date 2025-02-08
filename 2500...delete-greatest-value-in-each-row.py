class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        for i in range(r):
            grid[i].sort()
        sum = 0
        for i in range(c):
            mx = 0
            for j in range(r):
                mx = max(mx, grid[j][i])
            sum += mx
        return sum
