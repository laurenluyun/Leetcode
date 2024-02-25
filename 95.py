# -*- coding = utf-8 -*-
# @Time : 1/15/2024 1:35 AM
# @Author : Lauren
# @File : 95.py
# @Software : PyCharm

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        # return an empty list if number of nodes = 0
        if n == 0:
            return []
        # construct BST for [1, n]
        return self.build(1, n)

    def build(self, lo, hi):
        res = []
        # if lo > hi, exist no such node, restore None into the res[] and
        # return
        if lo > hi:
            res.append(None)
            return res
        # exhaust all the possibilities for the root, which can be any node
        # between lo and hi+1
        for i in range(lo, hi + 1):
            # construct the BST for left and right subtrees, lists are
            # returned
            leftTree = self.build(lo, i - 1)
            rightTree = self.build(i + 1, hi)
            # exhaust all the left and right subtree combinations for each
            # root
            for left in leftTree:
                for right in rightTree:
                    # i as the root val
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res


