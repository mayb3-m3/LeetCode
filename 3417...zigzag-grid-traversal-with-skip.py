class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n, arr, ans,  = len(grid), len(grid[0]), list(), list()
        for i in range(m):
            if i % 2:
                grid[i].reverse()
            arr += grid[i]
        for i in range(m*n):
            if i % 2 == 0:
                ans.append(arr[i])
        return ans
