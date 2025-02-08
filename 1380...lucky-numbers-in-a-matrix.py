class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans, m, n = list(), len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                mx, mn = 0, min(matrix[i])
                for k in range(m):
                    mx = max(mx, matrix[k][j])
                if mx == matrix[i][j] and mn == matrix[i][j]:
                    ans.append(matrix[i][j])
        return ans
