class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, mx = 0, -1e9
        sm = sum(nums[l:k-1])
        for i in range(k-1, len(nums)):
            sm += nums[i]
            mx = max(mx, sm/k)
            sm -= nums[l]
            l += 1
        return round(mx, 5)
