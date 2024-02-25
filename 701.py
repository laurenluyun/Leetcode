# -*- coding = utf-8 -*-
# @Time : 1/13/2024 6:06 PM
# @Author : Lauren
# @File : 701.py
# @Software : PyCharm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root, val: int):
        # find the blank space and insert the node with value val
        if root == None:
            return TreeNode(val)
        # search in the right subtree with recursion until root == None,
        # create the new node and return, update the roots one by one
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        # search for the left subtree...
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root
