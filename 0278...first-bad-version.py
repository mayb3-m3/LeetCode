class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r, ans = 1, n, n
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans
