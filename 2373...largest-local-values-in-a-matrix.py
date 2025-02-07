class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n-2) for i in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                mx = 0
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        mx = max(mx, grid[k][l])
                ans[i][j] = mx
        return ans
