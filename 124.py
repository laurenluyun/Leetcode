# -*- coding = utf-8 -*-
# @Time : 7/30/2023 11:09 AM
# @Author : Lauren
# @File : 124.py Binary Tree Maximum Path Sum
# key is path - each node cannot be visited twice ，DFS
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: [TreeNode]) -> int:
        '''
        81ms 98.75%, 23.96mb, 21.27%
        '''
        # to store the result of the maximum path sum
        res = [root.val]
        # return max path sum without split, takes a node as input and
        # returns the maximum path sum that can be achieved from that node
        # to its leaves
        def dfs(root):
            # base case
            if not root:
                return 0
            # recursively calls dfs on the left and right children of
            # current node and stores the results
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # then ensures they are non-negative, if it's negative, ignore it
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # compute max path sum with split
            res[0] = max(root.val + leftMax + rightMax, res[0])
            # the function returns the maximum sum that can be achieved
            # from the current node
            return root.val + max(leftMax, rightMax)
        # the dfs function is called on the root node to start the
        # computation of the maximum path sum for the entire binary tree
        dfs(root)
        return res[0]

