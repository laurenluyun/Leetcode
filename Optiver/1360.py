# -*- coding = utf-8 -*-
# @Time : 10/20/2023 10:33 PM
# @Author : Lauren
# @File : 1360.py
# @Software : PyCharm
# Number of Days Between Two Dates
from datetime import date


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def daysFrom1971(dt):
            y, m, d = int(dt[:4]), int(dt[5:7]), int(dt[8:])
            for i in range(1971, y):
                # leap year: can be evenly divided by 4 but not divided by 100
                # or is divisible by 400
                if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
                    d += 366
                else:
                    d += 365
            # leap year plus extra one day
            if (m > 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
                d += 1
            while m - 1 > 0:
                m -= 1
                d += days[m - 1]
            return d

        return abs(daysFrom1971(date1) - daysFrom1971(date2))
