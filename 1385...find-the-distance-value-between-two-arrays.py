class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in arr1:
            valid = 1
            for j in arr2:
                if abs(i-j) <= d:
                    valid = 0
                    break
            count += valid          
        return count
