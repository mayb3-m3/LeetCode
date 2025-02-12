class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        friq, candits, ans = [0] * (20000+1), list(), list()
        for num in nums:
            friq[num + 10000] += 1
        for i in range(len(friq)):
            candits.append((friq[i], i-10000))
        candits.sort(reverse = True)
        for i in range(k):
            ans.append(candits[i][1])
        return ans
