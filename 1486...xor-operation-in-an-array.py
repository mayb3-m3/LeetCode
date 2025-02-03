class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        for i in range(n):
            arr.append(start + 2*i)
        ans = 0
        for i in arr:
            ans ^= i
        return ans
