class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = list(s.split())
        ans = arr[0]
        for i in range(1, k):
            ans += " " + arr[i]
        return ans
