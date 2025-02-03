class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr, ans = date.split('-'), []
        for i in arr:
            ans.append(bin(int(i)))
        return str(ans[0])[2:] + "-" + str(ans[1])[2:] + "-" + str(ans[2])[2:]
