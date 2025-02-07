class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j or len(mat)-i-1 == j:
                    sum += mat[i][j]
        return sum
