# -*- coding = utf-8 -*-
# @Time : 5/29/2023 1:47 PM
# @Author : Lauren
# @File : 633.py
# @Software : PyCharm
'''
633. Sum of Square Numbers (Medium)
use two pointers
'''
from math import *

class Solution:
    '''
    340ms, 16.2mb
    '''
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(sqrt(c))

        if high ** 2 == c:
            return True

        while low <= high:
            x = low ** 2 + high ** 2
            if x == c:
                return True
            if x > c:
                high -= 1
            else:
                low += 1
        return False

class Solution1:
    '''
    390ms, 16.2mb
    '''
    def judgeSquareSum(self, c: int) -> bool:
        # use int(sqrt(c)) to reduce the run time
        for num in range(0, int(sqrt(c)) + 1):
            left = c - num ** 2
            # use int to avoid the 11 case, as sqrt(11)**2 = 11
            if left >= 0 and int(sqrt(left)) ** 2 == left:
                return True
        return False

def main():
    mySolution = Solution()
    c1 = 0
    c2 = 11
    c3 = 3
    print(mySolution.judgeSquareSum(c1))
    print(mySolution.judgeSquareSum(c2))
    print(mySolution.judgeSquareSum(c3))

if __name__ == "__main__":
    main()


