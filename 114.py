# -*- coding = utf-8 -*-
# @Time : 1/5/2024 10:13 PM
# @Author : Lauren
# @File : 114.py
# @Software : PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # base case
        if root == None:
            return

        # flatten the left and right branch
        self.flatten(root.left)
        self.flatten(root.right)

        # post order traverse, left and right are a linked list
        left = root.left
        right = root.right

        # left branch becomes right branch
        root.left = None
        root.right = left

        # connect the original right branch with the left branch
        p = root
        while p.right != None:
            p = p.right
        p.right = right
