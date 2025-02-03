class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dct = dict()
        for i in range(len(s)):
            dct[s[i]] = i
        sum = 0
        for i in range(len(s)):
            sum += abs(dct[t[i]] - i)
        return sum
