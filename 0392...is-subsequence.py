class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i1, i2, l1, l2 = 0, 0, len(s), len(t)
        while i1 < l1 and i2 < l2:
            if s[i1] == t[i2]:
                i1, i2 = i1+1, i2+1
            else:
                i2 += 1
        return i1 == l1
