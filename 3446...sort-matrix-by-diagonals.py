class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for k in range(n):
            i, j, arr = k, 0, list()
            while i < n and j < n:
                arr.append(grid[i][j])
                i, j = i+1, j+1
            arr.sort(reverse = True)
            i, j, pos = k, 0, 0
            while i < n and j < n:
                grid[i][j] = arr[pos]
                i, j, pos = i+1, j+1, pos+1
        for k in range(1, n):
            i, j, arr = 0, k, list()
            while i < n and j < n:
                arr.append(grid[i][j])
                i, j = i+1, j+1
            arr.sort()
            i, j, pos = 0, k, 0
            while i < n and j < n:
                grid[i][j] = arr[pos]
                i, j, pos = i+1, j+1, pos+1
        return grid
