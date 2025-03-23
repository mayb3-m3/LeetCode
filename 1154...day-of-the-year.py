import calendar
class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = int(date[0:4]), int(date[5:7]), int(date[8:])
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if calendar.isleap(y):
            days[1] = 29
        return sum(days[i] for i in range(m-1)) + d
