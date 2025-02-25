class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, posValue = 0, 1
        for i in range(len(columnTitle)-1, -1, -1):
            ans += (posValue*(ord(columnTitle[i]) - 64))
            posValue *= 26
        return ans
