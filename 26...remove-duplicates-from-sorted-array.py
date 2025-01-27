class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st = set(nums)
        st = sorted(st)
        idx = 0
        for i in st:
            nums[idx] = i
            idx += 1
        return len(st)
