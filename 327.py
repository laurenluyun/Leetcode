# -*- coding = utf-8 -*-
# @Time : 1/13/2024 12:32 AM
# @Author : Lauren
# @File : 327.py
# @Software : PyCharm

class Solution:
    def __init__(self):
        self.lo = 0
        self.hi = 0
        self.count = 0
        self.temp = []
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        self.lo = lower
        self.hi = upper

        # construct the presum array, NOTE: the length should be len(nums) + 1
        preSum = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            preSum[i + 1] = preSum[i] + nums[i]

        # use mergeSort on preSum
        self.temp = [0 for i in range(len(preSum))]
        self.sort(preSum, 0, len(preSum) - 1)
        return self.count

    def sort(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        self.sort(nums, lo, mid)
        self.sort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        for i in range(lo, hi + 1):
            self.temp[i] = nums[i]

        # improve the efficiency, maintain [start, end)
        start = mid + 1
        end = mid + 1
        for i in range(lo, mid + 1):
            # sliding window,所有符合要求的都在window里，只要计算end-start
            while start <= hi and nums[start] - nums[i] < self.lo:
                start += 1
            while end <= hi and nums[end] - nums[i] <= self.hi:
                end += 1
            self.count += end - start

        # merge by using 2 pointers
        i = lo
        j = mid + 1
        for p in range(lo, hi + 1):
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            elif j == hi + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1






