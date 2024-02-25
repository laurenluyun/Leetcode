# -*- coding = utf-8 -*-
# @Time : 12/30/2023 4:04 PM
# @Author : Lauren
# @File : 380.py
# @Software : PyCharm
import random


class RandomizedSet:

    def __init__(self):
        # store the values of each element in the nums list
        self.nums = []
        # store the val-index pair
        self.valToIndex = dict()

    # need to be O(1)
    def insert(self, val: int) -> bool:
        # no need to insert the val if val already exists
        if val in self.valToIndex:
            return False
        # if val does not exist, insert to the end of nums, and record its
        # index
        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True

    # need to be O(1)
    def remove(self, val: int) -> bool:
        # if val does not exist, no need to delete
        if val not in self.valToIndex:
            return False
        # get the index of val
        index = self.valToIndex[val]
        # change the index of the current rightmost element to index
        self.valToIndex[self.nums[-1]] = index
        # exchange val and the last element in nums
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        # delete val from nums at the end
        self.nums.pop()
        # delete val from map
        del self.valToIndex[val]
        return True

    # need to be O(1)
    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]
