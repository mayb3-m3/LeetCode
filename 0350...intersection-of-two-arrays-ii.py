class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = list()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    nums2[j] = 1001
                    break
        return ans
