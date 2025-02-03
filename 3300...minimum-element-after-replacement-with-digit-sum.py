class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num, sum = nums[i], 0
            while num:
                sum += (num%10)
                num //= 10
            nums[i] = sum
        return min(nums)
