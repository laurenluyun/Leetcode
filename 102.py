# -*- coding = utf-8 -*-
# @Time : 7/29/2023 11:09 AM
# @Author : Lauren
# @File : 102.py Binary Tree Level Order Traversal
# @Software : PyCharm
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: [TreeNode]) ->[List[int]]:
        '''
        BFS - need a queue, and each time insert an element to the right of
        the queue, and then pop element from the left of the queue [FIFO]
        1. traverse each level from left to right
        time complexity: O(n) we are only visiting each element a single time
        memory complexity: O(n)
        47ms, 94.39%, 17.21mb, 18.59%
        '''
        res = []
        # initialize a queue
        q = collections.deque()
        q.append(root)
        # keep traversing the q until there's no node left
        while q:
            qLen = len(q)
            level = []
            # the for loop controls each level contains only the nodes that
            # belong to the current level
            for i in range(qLen):
                # for each level, pop out the left node and restore in the
                # level list, then append its descendants to the q
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # if we want to add in the level, we want it to be non-empty
            if level:
                res.append(level)
        return res