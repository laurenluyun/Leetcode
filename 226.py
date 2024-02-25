# -*- coding = utf-8 -*-
# @Time : 7/26/2023 11:47 AM
# @Author : Lauren
# @File : 226.py Invert Binary Tree Easy
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        '''
        every time we visit a node, swap the positions of its children,
        do this recursively -> use DFS to solve this recursively
        '''
        # base case
        if not root:
            return None
        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        # do this recursively
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

class Solution1:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        if root == None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        # exchange left and right
        root.left = right
        root.right = left
        return root


def main():
    root1 = [4, 2, 7, 1, 3, 6, 9]
    root2 = [2, 1, 3]
    root3 = []


