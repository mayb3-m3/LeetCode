class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            temp = [1]
            for j in range(i):
                temp.append(ans[j] + ans[j+1])
            temp.append(1)
            ans = temp
        return ans
