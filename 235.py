# -*- coding = utf-8 -*-
# @Time : 7/28/2023 10:52 AM
# @Author : Lauren
# @File : 235.py Lowest Common Ancestor of a Binary Search Tree Medium
'''
can split the searching into left and right, if p or q is less than the
current node -> go to the left , otherwise -> go to the right
'''
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        O(log(n)) like binary search, because we only pick one node at each level
        63ms, 99.99%, 20.82mb, 57.87%
        '''
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur



