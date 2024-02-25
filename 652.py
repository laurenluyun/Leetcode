# -*- coding = utf-8 -*-
# @Time : 1/8/2024 9:40 AM
# @Author : Lauren
# @File : 652.py
# @Software : PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        res = []
        memo = {}

        def traverse(root):
            # '#' means end of the root / leaf
            if not root:
                return '#'

            left = traverse(root.left)
            right = traverse(root.right)

            # post order
            subTree = left + ',' + right + ',' + str(root.val)

            freq = memo.get(subTree, 0)
            # only append once to the res
            if freq == 1:
                res.append(root)
            # add the freq of the subtree
            memo[subTree] = freq + 1
            return subTree
        traverse(root)
        return res
