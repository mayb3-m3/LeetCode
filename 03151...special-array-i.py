class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        ans = True
        for i in range(1, len(nums)):
            if(nums[i-1] % 2 == nums[i] % 2):
                ans = False
                break
        return ans
