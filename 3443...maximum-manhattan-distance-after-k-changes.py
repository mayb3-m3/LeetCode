class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        north, south, east, west, ans = 0, 0, 0, 0, 0
        for ch in s:
            if ch == 'N':
                north += 1
            if ch == 'S':
                south += 1
            if ch == 'E':
                east += 1
            if ch == 'W':
                west += 1
            mn = min(north, south) + min(east, west)
            mx = max(north, south) + max(east, west)
            if mn <= k:
                ans = max(ans, mn+mx)
            else:
                ans = max(ans, mx+k - (mn-k))
        return ans
