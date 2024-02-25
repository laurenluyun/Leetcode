# -*- coding = utf-8 -*-
# @Time : 1/6/2024 3:27 PM
# @Author : Lauren
# @File : 106.py
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.valToIndex = {}
    def buildTree(self, inorder, postorder):
        for i in range(len(inorder)):
            self.valToIndex[inorder[i]] = i
        return self.build(inorder, 0, len(inorder) - 1, postorder, 0,
                          len(postorder) - 1)

    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd:
            return None
        rootVal = postorder[postEnd]
        index = self.valToIndex.get(rootVal)
        leftSize = index - inStart
        root = TreeNode(rootVal)
        # construct the left and right subtrees
        root.left = self.build(inorder, inStart, index - 1, postorder,
                               postStart, postStart + leftSize - 1)
        root.right = self.build(inorder, index + 1, inEnd, postorder,
                                postStart + leftSize, postEnd - 1)
        return root



