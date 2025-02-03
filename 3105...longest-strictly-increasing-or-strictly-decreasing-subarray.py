class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        mx1, mx2, l1, l2 = 0, 0, 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                l1 += 1
            else:
                mx1 = max(mx1, l1)
                l1 = 1
            if nums[i] < nums[i-1]:
                l2 += 1
            else:
                mx2 = max(mx2, l2)
                l2 = 1
        return max(mx1, mx2, l1, l2)
