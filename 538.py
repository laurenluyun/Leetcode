# -*- coding = utf-8 -*-
# @Time : 1/13/2024 3:59 PM
# @Author : Lauren
# @File : 538.py
# @Software : PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        # record the accumulated sum
        self.sum = 0
    def convertBST(self, root):
        self.traverse(root)
        return root
    def traverse(self, root):
        if root == None:
            return
        self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        self.traverse(root.left)

