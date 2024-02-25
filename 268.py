# -*- coding = utf-8 -*-
# @Time : 12/27/2023 1:32 PM
# @Author : Lauren
# @File : 268.py
# @Software : PyCharm

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res


