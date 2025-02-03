class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product, sum = 1, 0
        while n:
            product *= (n % 10)
            sum += (n % 10)
            n //= 10
        return product - sum
