class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, mid, hi = 0, 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if nums[mid] < target:
            return mid+1
        else:
            return mid
