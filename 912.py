# -*- coding = utf-8 -*-
# @Time : 1/10/2024 8:11 PM
# @Author : Lauren
# @File : 912.py
# @Software : PyCharm
class Solution:
    # construction with temp array to facilate merge sort
    def __init__(self):
        self.temp = []

    # call sort where the recursion is at
    def sortArray(self, nums: List[int]) -> List[int]:
        self.temp = [0 for i in range(len(nums))]
        self.sort(nums, 0, len(nums) - 1)
        return nums

    def sort(self, nums, lo, hi):
        if lo == hi:
            return
        # cut the nums in half and sort the left and right separately
        mid = lo + (hi - lo) // 2
        self.sort(nums, lo, mid)
        self.sort(nums, mid + 1, hi)
        # post-order postion
        self.merge(nums, lo, mid, hi)

    def merge(self, nums, lo, mid, hi):
        # copy all elements from nums to temp
        for i in range(lo, hi + 1):
            self.temp[i] = nums[i]

        # use 2 pointers to merge the 2 halves, i and j are the head of the 2 halves
        i = lo
        j = mid + 1
        for p in range(lo, hi + 1):
            # left half has been merged
            if i == mid + 1:
                nums[p] = self.temp[j]
                j += 1
            # right half has been merged
            elif j == hi + 1:
                nums[p] = self.temp[i]
                i += 1
            elif self.temp[i] > self.temp[j]:
                nums[p] = self.temp[j]
                j += 1
            else:
                nums[p] = self.temp[i]
                i += 1


