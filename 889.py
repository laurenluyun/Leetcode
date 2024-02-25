# -*- coding = utf-8 -*-
# @Time : 1/7/2024 12:45 AM
# @Author : Lauren
# @File : 889.py
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

    def constructFromPrePost(self, preorder, postorder):
        for i in range(len(postorder)):
            self.valToIndex[postorder[i]] = i

        return self.build(preorder, 0, len(preorder) - 1, postorder, 0,
                          len(postorder) - 1)

    def build(self, preorder, preStart, preEnd, postorder, postStart,
              postEnd):
        if preStart > preEnd:
            return None
        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        # the key is to get the range of the left and right branch of
        # preorder & postorder by getting the root of the left branch
        # the root would be the 1st element of the preorder
        rootVal = preorder[preStart]
        # KEY: the value of the root.left is the 2nd element of preorder
        leftRootVal = preorder[preStart + 1]
        # get the root of the left branch of the postorder
        index = self.valToIndex[leftRootVal]
        # get the left size
        leftSize = index - postStart + 1
        # recursion to construct the left and right branches
        root = TreeNode(rootVal)
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                               postorder, postStart, index)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                postorder, index + 1, postEnd - 1)
        return root



