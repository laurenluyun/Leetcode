# -*- coding = utf-8 -*-
# @Time : 7/27/2023 1:09 PM
# @Author : Lauren
# @File : 572.py Subtree of Another Tree
# Most tree problems are easier when you think about it recursively
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        '''
        recursive
        O(s * t), s is the total number of nodes of subRoot, t is the total number of
        nodes of the original root
        115ms, 91.53%, 17.55mb, 58.62%
        '''
        # base case
        if not subRoot: return True
        if not root: return False
        # will have to keep traversing through the tree even if the current
        # subRoot is not the same with the root
        if self.sameTree(root, subRoot):
            return True
        # recursive part
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(
            root.right, subRoot))


    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        return (self.sameTree(root.left, subRoot.left) and self.sameTree(
            root.right, subRoot.right))

