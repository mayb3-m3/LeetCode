class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        dct = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for ch in s:
            if ch in dct.values():
                ans.append(ch)
            elif ans and ans[-1] == dct.get(ch):
                ans.pop()
            else:
                return False
        return not ans
