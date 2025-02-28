class Solution:
    def longestPalindrome(self, s: str) -> int:
        friq, ans = dict(), 0
        for ch in s:
            if ch in friq:
                friq[ch] += 1
            else:
                friq[ch] = 1
        for val in friq.values():
            ans += (val//2)*2
        return ans + (ans != len(s))
