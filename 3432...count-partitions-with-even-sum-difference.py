class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        count, mx = 0, nums[-1]
        for i in range(0, len(nums)-1):
            left = nums[i]
            right = mx - nums[i]
            if (right - left) % 2 == 0:
                count += 1
        return count
