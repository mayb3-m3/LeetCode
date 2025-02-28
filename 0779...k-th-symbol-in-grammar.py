class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        val, mx = 0, 2**(n-1)
        for i in range(n-1):
            half = mx//2
            if k > half:
                val, k = 1 - val, k-half
            mx = half
        return val
