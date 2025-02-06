class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        fric = dict()
        for i in nums:
            if i in fric:
                fric[i] += 1
            else:
                fric[i] = 1
        for i in nums:
            if i + k in fric:
                count += fric[i+k]
            if i - k in fric:
                count += fric[i-k]
        return count//2 #because of i < j condition
