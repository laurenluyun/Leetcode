# -*- coding = utf-8 -*-
# @Time : 10/20/2023 11:37 PM
# @Author : Lauren
# @File : 1430.py
# @Software : PyCharm
# check if a string is a valid sequence from root to leaves path in a
# binary tree

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: list[int]) -> bool:
        def dfs(root, u):
            # if root is null or the list does not start from root node
            if root is None or root.val != arr[u]:
                return False
            # when the last element of arr is the leaf
            if u == len(arr) - 1:
                return root.left is None and root.right is None
            return dfs(root.left, u + 1) or dfs(root.right, u + 1)
        return dfs(root, 0)


