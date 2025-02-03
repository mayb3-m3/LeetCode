def subsets(main, subset, idx, sum):
    if idx == len(main):
        tot = 0
        for i in subset:
            tot ^= i
        sum[0] += tot
        return
    subsets(main, subset, idx+1, sum)
    subset.append(main[idx])
    subsets(main, subset, idx+1, sum)
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = [0]
        subsets(nums, [], 0, sum)
        return sum[0]
