class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1):
            lo, hi, found = i+1, len(nums)-1, False
            while lo <= hi:
                mid = (lo+hi)//2
                if nums[i] + nums[mid] < target:
                    found = True
                    if mid == len(nums)-1 or nums[i] + nums[mid+1] >= target:
                        count += mid - i
                        break
                    else:
                        lo = mid + 1
                else:
                    hi = mid - 1
            if found == False:
                break
        return count
