class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        st = set(bobSizes)
        alice, bob = sum(aliceSizes), sum(bobSizes)
        half = (alice+bob)//2 
        for i in aliceSizes:
            if (half - alice + i) in st:
                return [i, half - alice + i] 
