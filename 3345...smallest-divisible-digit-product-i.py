class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            temp = n
            while temp:
                product *= (temp % 10)
                temp //= 10
            if product % t == 0:
                return n
            n += 1
