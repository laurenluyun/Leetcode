# -*- coding = utf-8 -*-
# @Time : 12/30/2023 7:29 PM
# @Author : Lauren
# @File : 710.py
# @Software : PyCharm
import random


class Solution:
    def __init__(self, N, blacklist):
        # Calculate the size of the valid range by subtracting the length of
        # the blacklist from N and store it in the instance variable sz.
        self.sz = N - len(blacklist)
        # value - index
        self.mapping = {}
        # store all the blacklist elements in the map, to decide if the
        # number is in the blacklist
        for b in blacklist:
            self.mapping[b] = 666

        last = N - 1
        for b in blacklist:
            # if b is already in the range[sz, N), ignore it
            if b >= self.sz:
                continue

            # find a valid mapping for b, which is not in the blacklist
            # from end to start
            while last in self.mapping:
                last -= 1

            self.mapping[b] = last
            last -= 1
    def pick(self):
        # randomly select an index
        index = random.randint(0, self.sz - 1)
        # if the index is in the mapping(in the balcklist), return the mapped
        # value
        if index in self.mapping:
            return self.mapping[index]
        # if not in the mapping, return the index itself
        return index
