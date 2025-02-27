class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr1, arr2 = [0]*26, [0]*26
        for ch in s:
            arr1[ord(ch)-97] += 1
        for ch in t:
            arr2[ord(ch)-97] += 1
        for i in range(26):
            if arr1[i] != arr2[i]:
                return chr(97+i)
