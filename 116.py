# -*- coding = utf-8 -*-
# @Time : 1/5/2024 8:13 PM
# @Author : Lauren
# @File : 116.py
# @Software : PyCharm


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
traverse approach, binary tree becomes triple tree
'''
class Solution:
    def connect(self, root):
        if root == None:
            return None
        self.traverse(root.left, root.right)
        return root
    def traverse(self, node1, node2):
        if node1 == None or node2 == None:
            return
        # pre-order position: connect 2 nodes
        node1.next = node2
        # connect the left right nodes of the same root
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        # connect the two child branches
        self.traverse(node1.right, node2.left)


