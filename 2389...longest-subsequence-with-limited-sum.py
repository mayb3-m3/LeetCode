class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = list()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        for target in queries:
            l, r, mx = 0, len(nums)-1, 0
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    mx = mid+1
                    break
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    mx = max(mx, mid+1)
                    l = mid + 1
            ans.append(mx)
        return ans
