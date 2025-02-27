class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = [0] * 26
        for ch in s:
            arr[ord(ch)-97] += 1
        for i in range(len(s)):
            if arr[ord(s[i])-97] == 1:
                return i
        return -1
