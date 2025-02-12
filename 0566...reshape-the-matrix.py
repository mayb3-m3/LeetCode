class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n == r*c:
            pos, arr, ans = 0, list(), [[0] * c for i in range(r)]
            arr = [item for rows in mat for item in rows]
            for i in range(r):
                for j in range(c):
                    ans[i][j] = arr[pos]
                    pos += 1
            return ans
        else:
            return mat
