class Solution:
    def check(self, nums: List[int]) -> bool:
        part = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                part += 1
        if part == 0:
            return True
        if part == 1 and nums[0] >= nums[-1]:
            return True
        return False
