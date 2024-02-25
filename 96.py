# -*- coding = utf-8 -*-
# @Time : 1/15/2024 2:31 AM
# @Author : Lauren
# @File : 96.py
# @Software : PyCharm
class Solution:
    def __init__(self):
        # memo
        self.memo = []

    def numTrees(self, n: int) -> int:
        # initialize memo to 0
        self.memo = [[0] * (n+1) for _ in range(n+1)]
        return self.count(1, n)

    def count(self, lo, hi):
        if lo > hi:
            return 1
        # search the memo to avoid duplicate res
        if self.memo[lo][hi] != 0:
            return self.memo[lo][hi]

        res = 0
        for mid in range(lo, hi+1):
            left = self.count(lo, mid - 1)
            right = self.count(mid+1, hi)
            res += left * right

        # record the res into memo
        self.memo[lo][hi] = res
        return res
