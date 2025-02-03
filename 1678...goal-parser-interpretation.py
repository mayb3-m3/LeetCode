class Solution:
    def interpret(self, command: str) -> str:
        idx, ans = 0, ""
        while idx < len(command):
            if command[idx] == 'G':
                ans += 'G'
                idx += 1
            elif command[idx] == '(' and command[idx+1] == ')':
                ans += 'o'
                idx += 2
            else:
                ans += "al"
                idx += 4
        return ans
