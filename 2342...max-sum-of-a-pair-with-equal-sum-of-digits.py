class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dct, mx = dict(), -1
        for i in range(len(nums)):
            num, sum = nums[i], 0
            while num:
                sum += num % 10
                num //= 10
            if sum in dct:
                mx = max(mx, dct[sum]+nums[i])
                dct[sum] = max(dct[sum], nums[i])
            else:
                dct[sum] = nums[i]
        return mx
