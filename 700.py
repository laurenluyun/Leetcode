# -*- coding = utf-8 -*-
# @Time : 1/13/2024 5:44 PM
# @Author : Lauren
# @File : 700.py
# @Software : PyCharm

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root, val: int):
        if root == None:
            return None
        # search the left subtree
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)
        return root
