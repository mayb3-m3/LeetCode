class Solution:
    def judgeCircle(self, moves: str) -> bool:
        sum1, sum2 = 0, 0
        for ch in moves:
            if ch == 'U':
                sum1 += 1
            elif ch == 'D':
                sum1 -= 1
            elif ch == 'R':
                sum2 += 1
            else:
                sum2 -= 1
        return sum1 == 0 and sum2 == 0
