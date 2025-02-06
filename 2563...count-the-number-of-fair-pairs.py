import bisect
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1):
            idx1 = bisect.bisect_left(nums, lower - nums[i], i + 1)
            idx2 = bisect.bisect_right(nums, upper - nums[i], i + 1)
            count += idx2 - idx1
        return count
