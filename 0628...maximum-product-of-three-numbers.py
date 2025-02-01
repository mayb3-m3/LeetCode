class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        s = sorted(nums)
        a = s[-1]*s[-2]*s[-3]
        b = s[0]*s[1]*s[-1]
        return max(a, b)
