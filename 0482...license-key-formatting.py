class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(s.split('-')).upper()
        l = len(s)
        s1, s2 = s[0:l%k], s[l%k:]
        if len(s1):
            return '-'.join([s1] + [s2[i:i+k] for i in range(0, len(s2), k)])
        else:
            return '-'.join([s2[i:i+k] for i in range(0, len(s2), k)])
