class Solution:
    def validPalindrome(self, s: str) -> bool:
        f, b = 0, len(s)-1
        op1, op2 = "", ""
        while f <= b:
            if s[f] == s[b]:
                f += 1
                b -= 1
            else:
                op1 = s[0:f] + s[f+1:]
                op2 = s[0:b] + s[b+1:]
                break
        r1 = op1[::-1]
        r2 = op2[::-1]
        return op1 == r1 or op2 == r2
