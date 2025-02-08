class NeighborSum:
    def sum(self, fr, fc, value):
        n, tot = len(self.arr), 0
        for i in range(n):
            for j in range(n):
                if self.arr[i][j] == value:
                    for k in range(4):
                        x, y = i+fr[k], j+fc[k]
                        if x >= 0 and y >= 0 and x < n and y < n:
                            tot += self.arr[x][y]
                    return tot
    def __init__(self, grid: List[List[int]]):
        self.arr = grid
    def adjacentSum(self, value: int) -> int:
        return self.sum([1, 0, -1, 0], [0, 1, 0, -1], value)
    def diagonalSum(self, value: int) -> int:
        return self.sum([1, 1, -1, -1], [1, -1, 1, -1], value)
