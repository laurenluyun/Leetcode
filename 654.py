# -*- coding = utf-8 -*-
# @Time : 1/6/2024 1:18 PM
# @Author : Lauren
# @File : 654.py
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums):
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, lo, hi):
        # base case
        if lo > hi:
            return None

        # find the index of the maximum value in the current array
        index, max_val = -1, float('-inf')
        for i in range(lo, hi + 1):
            if max_val < nums[i]:
                index = i
                max_val = nums[i]

        # construct the root node
        root = TreeNode(max_val)

        # recursively build the left and right subtree
        root.left = self.build(nums, lo, index - 1)
        root.right = self.build(nums, index + 1, hi)

        return root


