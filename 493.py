# -*- coding = utf-8 -*-
# @Time : 1/11/2024 12:15 AM
# @Author : Lauren
# @File : 493.py
# @Software : PyCharm

class Solution:
    def __init__(self):
        self.count = 0
        self.temp = []

    def reversePairs(self, nums: list[int]) -> int:
        # call mergesort
        n = len(nums)
        self.temp = [0 for i in range(n)]
        self.sort(nums, 0, n - 1)
        return self.count

    def sort(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        self.sort(nums, lo, mid)
        self.sort(nums, mid + 1, hi)
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        # copy to the temp
        for i in range(lo, hi + 1):
            self.temp[i] = nums[i]

        # 效率优化，维护左闭右开区间[mid+1, end)中的元素*2 < nums[i], 左闭右开是因为可以保证初始区间[mid+1,
        # mid+1) 是一个空区间
        end = mid + 1
        # count for each i from (lo, mid), each element will compare each
        # element in the second half
        for i in range(lo, mid + 1):
            while end <= hi and nums[i] > nums[end] * 2:
                end += 1
            self.count += end - (mid + 1)

        # merge the 2 halves using 2 pointers
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


