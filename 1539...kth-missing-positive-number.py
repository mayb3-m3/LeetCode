class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing, mn = [], len(arr)
        for i in range(len(arr)):
            missing.append(arr[i]-i-1)
        l, r = 0, len(missing)-1
        while(l <= r):
            mid = (l+r)//2
            if missing[mid] >= k:
                mn = min(mn, mid)
                r = mid - 1
            else:
                l = mid + 1
        if mn == len(arr):
            return arr[-1] + k - missing[-1]
        else:
            return arr[mn] - (missing[mn]+1) + k
