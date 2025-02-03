class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1 = "000" + str(num1)
        s2 = "000" + str(num2)
        s3 = "000" + str(num3)
        ans = ""
        for i in range(-1, -5, -1):
            ans = min(s1[i], s2[i], s3[i]) + ans
        return int(ans)
