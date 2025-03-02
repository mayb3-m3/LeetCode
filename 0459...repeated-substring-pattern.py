class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub, n = "", len(s)
        for i in range(n//2):
            sub += s[i]
            if n % (i+1) == 0 and sub * (n//(i+1)) == s:
                return True
        return False
