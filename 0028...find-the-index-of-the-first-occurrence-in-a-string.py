class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1, l2 = len(haystack), len(needle)
        index = -1
        if l1 >= l2:
            for i in range(0, l1-l2+1):
                if(haystack[i:i+l2] == needle):
                    index = i
                    break
        return index
