# -*- coding = utf-8 -*-
# @Time : 1/4/2024 6:36 PM
# @Author : Lauren
# @File : 543.py
# @Software : PyCharm

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root) -> int:
        self.maxDepth(root)
        return self.maxDiameter
    # 分解思维
    def maxDepth(self, root):
        if root == None:
            return 0
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # post-order position, and calculate the max diameter
        myDiameter = leftMax + rightMax
        self.maxDiameter = max(self.maxDiameter, myDiameter)
        return 1 + max(leftMax, rightMax)

