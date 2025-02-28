class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        if n1 < n2:
            num1 = "0"*(n2-n1) + num1
        else:
            num2 = "0"*(n1-n2) + num2
        carry, n, ans = 0, max(n1, n2), ""
        for i in range(n):
            sum = carry + int(num1[n-1-i]) + int(num2[n-1-i])
            ans += str(sum%10)
            carry = sum//10
        if carry:
            ans += str(carry)
        return ans[::-1]
