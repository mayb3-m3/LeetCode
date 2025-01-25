class Solution:
    def isValid(self, s: str) -> bool:
        ans = ""
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                ans += ch
            elif ans:
                if ch == ')' and ans[-1] == '(':
                    ans = ans[:-1]
                elif ch == '}' and ans[-1] == '{':
                    ans = ans[:-1]
                elif ch == ']' and ans[-1] == '[':
                    ans = ans[:-1]
                else:   
                    return False
            else:
                return False
        if ans:
            return False
        else:
            return True
