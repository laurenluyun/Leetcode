# -*- coding = utf-8 -*-
# @Time : 7/29/2023 1:17 PM
# @Author : Lauren
# @File : 230.py Kth Smallest Element in a BST
# @Software : PyCharm


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        '''
        node.left < node.val < node.right
        traverse the BST and put the elements in an array in ascending order
        iterative approach: we need a stack to contain the previous node
        that we need to pop back up to
        every time we pop an element that means we are processing /
        visiting it, then we visit its right node
        so that we can visit the elements in ascending order
        51ms, 98.83%, 20.48mb, 52.28%
        '''
        stack = []
        cur = root # pointer telling us which node we are currently visiting
        while cur or stack:
            while cur:
                # we are going to go left as much as we can
                stack.append(cur)
                cur = cur.left
            # pop out the cur means we are processing it
            cur = stack.pop()
            k -= 1
            if k == 0:
                # this line will be executed ultimately
                return cur.val
            cur = cur.right

class Solution1:
    def __init__(self):
        self.res = 0
        self.rank = 0

    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        self.traverse(root, k)
        return self.res

    def traverse(self, root, k):
        if root == None:
            return
        self.traverse(root.left, k)
        # process at the in-order position
        self.rank += 1
        if k == self.rank:
            self.res = root.val
            return
        self.traverse(root.right, k)


