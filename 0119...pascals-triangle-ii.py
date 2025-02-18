import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex+1):
            ans.append(factorial(rowIndex)//(factorial(i)*factorial(rowIndex-i)))
        return ans
