class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0]*26
        for ch in magazine:
            arr[ord(ch)-97] += 1
        for ch in ransomNote:
            if arr[ord(ch)-97]:
                arr[ord(ch)-97] -= 1
            else:
                return False
        return True
