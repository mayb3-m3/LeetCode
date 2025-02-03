class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        sum = 0
        while additionalTank and mainTank >= 5:
            sum += 5
            mainTank -= 4
            additionalTank -= 1
        sum += mainTank
        return 10 * sum
