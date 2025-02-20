class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums, ans = [1] * 2001, []
        nums[0] = 0
        for i in arr:
            nums[i] = 0
        for i in range(2001):
            if nums[i]:
                ans.append(i)
        return ans[k-1]
