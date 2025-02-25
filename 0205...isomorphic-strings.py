class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct1, dct2 = dict(), dict()
        for i in range(len(s)):
            if s[i] in dct1 and dct1[s[i]] != t[i]:
                return False
            else:
                dct1[s[i]] = t[i]
            if t[i] in dct2 and dct2[t[i]] != s[i]:
                return False
            else:
                dct2[t[i]] = s[i]
        return True
