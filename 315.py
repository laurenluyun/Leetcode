# -*- coding = utf-8 -*-
# @Time : 1/10/2024 9:18 PM
# @Author : Lauren
# @File : 315.py
# @Software : PyCharm

class Pair:
    def __init__(self, val, id):
        # 在排序过程中，每个元素的索引位置会不断改变，所以我们⽤⼀个 Pair 类封装每个元素及其在原始数
        # 组 nums 中的索引，以便 count 数组记录每个元素之后⼩于它的元素个数
        self.val = val
        self.id = id

class Solution:
    def __init__(self):
        # construction with temp array to facilate merge sort
        self.temp = []
        # result
        self.count = []

    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        self.count = [0 for i in range(n)]
        self.temp = [0 for i in range(n)]
        arr = []
        # record the original index of each element to update count
        for i in range(n):
            arr.append(Pair(nums[i], i))

        # call the mergesort and restore in the count
        self.sort(arr, 0, n - 1)

        return self.count

    def sort(self, arr, lo, hi):
        if lo == hi:
            return
        mid = lo + (hi - lo) // 2
        self.sort(arr, lo, mid)
        self.sort(arr, mid + 1, hi)
        self.merge(arr, lo, mid, hi)

    def merge(self, arr, lo, mid, hi):
        # copy all elements from arr to temp
        for i in range(lo, hi + 1):
            self.temp[i] = arr[i]
        i = lo
        j = mid + 1
        for p in range(lo, hi + 1):
            if i == mid + 1:
                arr[p] = self.temp[j]
                j += 1
            elif j == hi + 1:
                arr[p] = self.temp[i]
                i += 1
                # update count
                # 每当执⾏ nums[p] = temp[i]时，就可以确定 temp[i] 这个元素后⾯⽐它⼩的元素个数为 j -
                # mid - 1。
                self.count[arr[p].id] += j - (mid + 1)

            elif self.temp[i].val > self.temp[j].val:
                arr[p] = self.temp[j]
                j += 1
            else:
                arr[p] = self.temp[i]
                i += 1
                # update count
                # 每当执⾏ nums[p] = temp[i]时，就可以确定 temp[i] 这个元素后⾯⽐它⼩的元素个数为 j -
                # mid - 1。
                self.count[arr[p].id] += j - (mid + 1)




