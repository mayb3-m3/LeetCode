class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        arr = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                arr.append(s1[i])
                arr.append(s2[i])
        if len(arr) == 4 and arr[0] == arr[3] and arr[1] == arr[2]:
            return True
        return False
