# -*- coding = utf-8 -*-
# @Time : 1/5/2024 6:28 PM
# @Author : Lauren
# @File : BFS_BTrecursion.py
# @Software : PyCharm

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def level_traverse(self, root):
        if not root:
            return self.res
        # root is considered as level 0
        self.traverse(root, 0)
        return self.res

    def traverse(self, root, depth):
        if not root:
            return
        # add depth number of levels in the list res
        if len(self.res) <= depth:
            self.res.append([])
        # Add the value of the current node to the list at the current depth
        self.res[depth].append(root.val)
        #Recursive calls for the left and rifht children with increased depth
        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)

class Solution2:
    def __init__(self):
        self.res = []

    def level_traverse(self, root):
        if not root:
            return self.res
        nodes = [root]
        self.traverse(nodes)
        return self.res

    def traverse(self, cur_level_nodes):
        # base case
        if not cur_level_nodes:
            return
        # pre-order position, calculate the values of the current level and
        # the next level's node list
        node_values = []
        next_level_nodes = []
        for node in cur_level_nodes:
            node_values.append(node.val)
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        # pre-order position to add the result, yielding a top-down level
        # order traversal
        self.res.append(node_values)
        self.traverse(next_level_nodes)
        # post-order position to add the result, yielding a bottom-up level
        # order traversal
        # self.res.append(node_values)
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    solution = Solution()
    result = solution.level_traverse(root)
    for i, level in enumerate(result):
        print(f"Level {i}: {level}")

if __name__ == "__main__":
    main()
