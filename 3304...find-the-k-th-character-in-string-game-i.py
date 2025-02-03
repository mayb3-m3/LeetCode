class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            temp = ""
            for ch in s:
                temp += chr(97 + (ord(ch)-ord('a')+1)%26)
            s += temp
        return s[k-1]
