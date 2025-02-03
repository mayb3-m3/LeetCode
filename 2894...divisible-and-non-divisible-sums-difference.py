class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum = n*(n+1)//2
        num1, num2 = sum, 0
        for i in range(m, n+1, m):
            num1 -= i
            num2 += i
        return num1 - num2
