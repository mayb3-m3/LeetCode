class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for s in sentences:
            mx = max(mx, len(s.split()))
        return mx
