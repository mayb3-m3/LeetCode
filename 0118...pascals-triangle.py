class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            temp, prev = [1], ans[-1]
            for j in range(i):
                temp.append(prev[j]+prev[j+1])
            temp.append(1)
            ans.append(temp)
        return ans
