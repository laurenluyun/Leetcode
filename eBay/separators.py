# -*- coding = utf-8 -*-
# @Time : 10/25/2023 12:26 PM
# @Author : Lauren
# @File : separators.py
# @Software : PyCharm
import math
from sortedcontainers import SortedList
from typing import List


def min_diff(nums: List, sep: int):
    ln = len(nums)
    sl = SortedList(nums[sep:])

    res = math.inf
    for i in range(0, ln-sep):
        if i > 0:
            sl.discard(nums[i+sep-1])
            # It is used to find the index at which an element should be
            # inserted into a sorted list while maintaining its sorted order.
        j = sl.bisect_right(nums[i])
        if j < len(sl):
            res = min(res, sl[j] - nums[i])
        if j > 0:
            res = min(res, nums[i] - sl[j-1])

    return res

    # res, l = float('inf'), SortedList([-float('inf'), float('inf')]
    # for i in range(len(nums) - 1, sep - 2, -1):
    #     l.add(nums[i])
    #     i-= sep + 1
    #     j = l.bisect_right(nums[i])
    #     res = min([res, nums[i] - nums[j - 1], nums[j] - nums[i]])
    # return res


if __name__ == '__main__':
    print(min_diff([1,5,4,10,9], 3))   # 4: |5 - 9|
    print(min_diff([1,5,4,10,91,54,20,8], 3))   # 2: |10 - 8|

