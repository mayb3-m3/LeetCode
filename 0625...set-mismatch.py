class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums)+1)
        for i in nums:
            ans[i] += 1
        a, b = 0, 0
        for i in range(1, len(nums)+1):
            if ans[i] == 0:
                b = i
            if ans[i] == 2:
                a = i
        return [a, b]
