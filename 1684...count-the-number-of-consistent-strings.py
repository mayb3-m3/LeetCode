class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for s in words:
            is_present = True
            for ch in s:
                if ch not in allowed:
                    is_present = False
            if is_present:
                count += 1
        return count
