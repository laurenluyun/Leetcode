# -*- coding = utf-8 -*-
# @Time : 7/27/2023 8:42 AM
# @Author : Lauren
# @File : 104.py Maximum Depth of Binary Tree
# three ways: recursive DFS, iterative DFS, BFS
# @Software : PyCharm

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def __init__(self):
        self.res = 0
        self.depth = 0
    def maxDepth(self, root):
        self.traverse(root)
        return self.res
    def traverse(self, root):
        # If the current node is None, return 0 (base case)
        if root == None:
            return 0
        # Increment the current depth.  The depth values continue to
        # accumulate as the traversal goes deeper into the tree.
        self.depth += 1
        # If the current node is a leaf node (both left and right children are None),
        # update the result with the maximum depth encountered so far
        if root.left == None and root.right == None:
            self.res = max(self.res, self.depth)
        # Recursively traverse the left and right subtrees
        self.traverse(root.left)
        self.traverse(root.right)
        # Backtrack: Decrement the depth when returning from a subtree to a
        # parent node which has already been visited
        self.depth -= 1

class Solution2:
    def maxDepth(self, root):
        # base case: If the current node is None, return 0
        if root == None:
            return 0
        # Recursive calls to find the maximum depth of the left and right subtrees
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # The + 1 accounts for the depth of the current node itself.
        res = max(leftMax, rightMax) + 1
        return res

class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        '''
        recursive DFS
        Time and memory complexity: O(n)
        34ms, 99.96%, 18.76mb, 34.13%
        '''
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth01(self, root: [TreeNode]) -> int:
        '''
        BFS
        Time and memory complexity: O(n)
        deque: double-ended queue data structure is a versatile data
        structure that allows efficient insertion and deletion from both ends
        from collections import deque

        1. Creating an empty deque
        my_deque = deque()

        2. Adding elements to the deque from the right end
        my_deque.append(10)
        my_deque.append(20)
        my_deque.append(30)

        3. Adding elements to the deque from the left end
        my_deque.appendleft(5)
        my_deque.appendleft(2)

        4. Printing the deque
        print(my_deque)  # Output: deque([2, 5, 10, 20, 30])

        5. Removing elements from the right end
        my_deque.pop()   # Removes and returns 30

        6. Removing elements from the left end
        my_deque.popleft()   # Removes and returns 2

        7. Printing the updated deque
        print(my_deque)  # Output: deque([5, 10, 20])

        '''
        if not root:
            return 0
        # keep track of the number of levels of the tree during traversal
        level = 0
        # create a deque and enqueues the root node to start the BFS traversal
        q = deque([root])
        # while loop until the deque is not empty, this loop represents BFS
        # traversal
        while q:
            # nested for loop is used to process all the nodes at the
            # current level
            for i in range(len(q)):
                # for each level, it dequeues a node from the left end of
                # the deque and checks if it has left and /or right
                # children. If so, it enqueues these children nodes to q
                # from right end for further processing in the next level
                # each time dequeues the extreme left node, and append its
                # children to the queue, level += 1, next time pop the
                # extreme left node of the queue, and append its children
                # again....until the queue is empty
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    def maxDepth03(self, root: [TreeNode]) -> int:
        '''
        iterative DFS using stack data structure
        '''
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res







