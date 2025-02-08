class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row, mx = 0, 0
        for i in range(len(mat)):
            count = mat[i].count(1)
            if count > mx:
                row, mx = i, count
        return [row, mx]
