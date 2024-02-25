# -*- coding = utf-8 -*-
# @Time : 5/31/2023 9:44 AM
# @Author : Lauren
# @File : 69.py
# @Software : PyCharm
'''
Sqrt(x)
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Use Binary Search 50ms, 16.3mb
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            sqrt = x // mid
            if sqrt == mid:
                return mid
            elif sqrt < mid:
                right = mid - 1
            else:
                left = mid + 1
        return right

class Solution1:
    # 牛顿迭代法 55ms, 16.2mb
    def mySqrt(self, x: int) -> int:
        sqrt = x
        while sqrt * sqrt > x:
            sqrt = (sqrt + x / sqrt) // 2
        return round(sqrt)

def main():
    mySolution = Solution()
    x1 = 20
    x2 = 3
    x3 = 110
    print(mySolution.mySqrt(x1))
    print(mySolution.mySqrt(x2))
    print(mySolution.mySqrt(x3))


if __name__ == "__main__":
    main()

