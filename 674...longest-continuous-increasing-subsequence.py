class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans, cnt, i = 1, 1, 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
            i += 1
        return max(ans, cnt)
