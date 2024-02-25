# -*- coding = utf-8 -*-
# @Time : 7/29/2023 2:56 PM
# @Author : Lauren
# @File : 105.py Construct Binary Tree from Preorder and Inorder Traversal
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder) -> [TreeNode]:
        '''
        preorder traversal: BFS, the list always starts with the root
        Inorder: visit all the nodes in the left, and then the root itself,
        then all the nodes on the right => DFS
        recursion
        165ms, 68.56%, 90.79mb, 44.51%
        '''
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        # the root is in the middle of the inorder list
        mid = inorder.index(preorder[0])
        # create the sublist using recursion
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

class Solution1:
    def __init__(self):
        self.valToIndex = {}
    def buildTree(self, preorder, inorder) -> [TreeNode]:
        for i in range(len(inorder)):
            self.valToIndex[inorder[i]] = i
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0,
                          len(inorder) - 1)
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd:
            return None
        # root is the first element of preorder
        rootVal =preorder[preStart]
        index = self.valToIndex.get(rootVal)
        leftSize = index - inStart

        # construct the root node
        root = TreeNode(rootVal)
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,\
                    inorder, inStart, index - 1)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                inorder, index + 1, inEnd)
        return root

