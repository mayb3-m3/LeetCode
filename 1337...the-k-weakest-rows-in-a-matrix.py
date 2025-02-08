class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n, ans = len(mat), len(mat[0]), list()
        for i in range(m):
            ans.append([mat[i].count(1), i])
        ans.sort()
        return [every[1] for every in ans[:k]]
