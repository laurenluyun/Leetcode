# -*- coding = utf-8 -*-
# @Time : 1/15/2024 1:07 PM
# @Author : Lauren
# @File : 1373.py
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
1.左右子树是否是ST 2.左子树的最大值和右子树的最小值3.左右子树的节点值之和
res[0]记录是否是BST，是则1，不是则0
res[1]记录以root为根的二叉树所有节点的最小值
res[2]记录以root为根的二叉树所有节点的最大值
time complexity O(n)

'''
class Solution:
    def __init__(self):
        self.maxSum = 0
    def maxSumBST(self, root) -> int:
        self.findMaxMinSum(root)
        return self.maxSum

    def findMaxMinSum(self, root):
        # base case
        if root == None:
            return [1, float('inf'), float('-inf'), 0]

        # cal the left and right subtrees with recursion
        left = self.findMaxMinSum(root.left)
        right = self.findMaxMinSum(root.right)

        # post order
        res = [0 for i in range(4)]
        # if statement to decide if the left and right subtrees are BST
        if left[0] == 1 and right[0] == 1 and root.val > left[2] and \
                root.val < right[1]:
            # root based tree is BST
            res[0] = 1
            '''
            these comparisons are added to handle edge cases where the 
            left or right subtree is empty. left[2] and right[1] would be set 
            to positive and negative infinity, respectively, during the 
            recursive calls. Therefore, comparing with root.val ensures 
            that if one of the subtrees is empty, it doesn't incorrectly 
            contribute to the minimum or maximum values of the current subtree
            '''
            # cal the min value of this BST: left[1]is min of left
            res[1] = min(left[1], root.val)
            # cal the max value of this BST: right[2]is max of right
            res[2] = max(right[2], root.val)
            # cal the sum of all nodes
            res[3] = left[3] + right[3] + root.val
            # update the maxSum
            self.maxSum = max(self.maxSum, res[3])
        else:
            # the tree with root is not a BST, can leave other attributes
            # bank
            res[0] = 0
        return res





