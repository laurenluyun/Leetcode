# -*- coding = utf-8 -*-
# @Time : 7/29/2023 12:50 PM
# @Author : Lauren
# @File : 98.py Validate Binary Search Tree
# @Software : PyCharm

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: [TreeNode]) -> bool:
        '''
        O(n) recursion
        39ms, 99.9%, 18.76mb, 79.64%
        '''
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, node, left, right):
        if not node:
            return True
        if not (node.val < right and node.val > left):
            return False
        return (self.valid(node.left, left, node.val) and self.valid(
            node.right, node.val, right))

class Solution1:
    def isValidBST(self, root) -> bool:
        return self.validBST(root, None, None)

    # require that the subtree with root must satisfy: max.val > root.val >
    # min.val
    def validBST(self, root, min, max):
        # base case
        if root == None:
            return True
        # if the root.val <= min.val => not a valid BST
        if min != None and root.val <= min.val:
            return False
        if max != None and root.val >= max.val:
            return False
        # the max value of the left subtree is root.val, the min value of
        # right subtree is root
        return self.validBST(root.left, min, root) and self.validBST(
            root.right, root, max)

