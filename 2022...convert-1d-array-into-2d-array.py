class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans, idx = [[0] * n for i in range(m)], 0
        if m*n == len(original):
            for i in range(m):
                for j in range(n):
                    ans[i][j] = original[idx]
                    idx += 1
        if ans[0][0] >= 1:
            return ans
        return []
