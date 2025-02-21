class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        st, ans = set(nums2), 10**10
        for i in nums1:
            if i in st:
                ans = min(ans, i)
        if ans == 10**10:
            return -1
        return ans
