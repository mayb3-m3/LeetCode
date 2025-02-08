class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            count = 0
            for j in range(len(grid)):
                if grid[i][j] == 1 and i != j:
                    count += 1
            if count == len(grid)-1:
                return i
