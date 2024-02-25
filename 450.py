# -*- coding = utf-8 -*-
# @Time : 1/13/2024 8:52 PM
# @Author : Lauren
# @File : 450.py
# @Software : PyCharm

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key: int):
        if root == None:
            return None
        if root.val == key:
            # 1st and 2nd scenario
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            # 3rd scenario
            # get the min node of the right subtree
            minNode = self.getMin(root.right)
            # get to the root in the right subtree which has the min value
            root.right = self.deleteNode(root.right, minNode.val)
            # replace the minNode left and right with root's
            minNode.left = root.left
            minNode.right = root.right
            # replace root with minNode, here minNode has root's subtrees
            # but with its own val
            root = minNode

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

    def getMin(self, node):
        # the left most node of BST is the min node
        while node.left != None:
            node = node.left
        return node


