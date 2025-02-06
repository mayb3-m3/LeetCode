class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dct = dict()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                mul = nums[i] * nums[j]
                if mul in dct:
                    dct[mul] += 1
                else:
                    dct[mul] = 1
        count = 0
        for i in dct.values():
            count += (i*(i-1)//2) * 8
        return count
