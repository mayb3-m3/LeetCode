class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r, count = 0, 0, 0
        for ch in s:
            if ch == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                count += 1
                l, r = 0, 0
        return count 
