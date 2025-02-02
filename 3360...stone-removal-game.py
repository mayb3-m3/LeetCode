class Solution:
    def canAliceWin(self, n: int) -> bool:
        value = 10
        for i in range(1, 10):
            if i % 2 == 1 and n < value:
                return False
            elif i % 2 == 0 and n < value:
                return True
            n -= value
            value -= 1
