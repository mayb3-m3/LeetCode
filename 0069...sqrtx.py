class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, 1e6
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                return int(mid)
            elif mid*mid < x:
                lo = mid + 1
            else:
                hi = mid - 1
