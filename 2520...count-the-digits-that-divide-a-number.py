class Solution:
    def countDigits(self, num: int) -> int:
        copy, count = num, 0
        while copy:
            if num % (copy % 10) == 0:
                count += 1
            copy //= 10
        return count
