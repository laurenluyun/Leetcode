# -*- coding = utf-8 -*-
# @Time : 1/10/2024 6:21 PM
# @Author : Lauren
# @File : mergesort.py
# @Software : PyCharm

class mergeSort:
    def __init__(self):
        self.temp = []

    def mergeSort(self, nums):
        self.temp = [0 for i in range(len(nums))]
        self.sort(nums, 0, len(nums) - 1)
        return nums

    def sort(self, nums, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        # sort nums[lo...mid]
        self.sort(nums, lo, mid)
        # sort nums[mid + 1...hi]
        self.sort(nums, mid + 1, hi)
        # post-order position, right now the 2 parts of the list have been
        # sorted, then merge the two
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        # merge nums[lo..mid] and nums[mid+1..hi] into nums[lo,hi]
        # copy nums element to the temp
        for i in range(lo, hi + 1):
            self.temp[i] = nums[i]

        # use 2 pointers to merge 2 sorted arrays合并两个有序链表到nums[lo..hi]
        # i j 分别是 两个有序array的头子，拉链法
        i = lo
        j = mid + 1
        for p in range(lo, hi + 1):
            # left half has been merged, use the right half
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            # right half has all been merged, use the left half
            elif j == hi + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1
