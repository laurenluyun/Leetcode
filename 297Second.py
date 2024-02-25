# -*- coding = utf-8 -*-
# @Time : 1/7/2024 8:38 PM
# @Author : Lauren
# @File : 297Second.py
# @Software : PyCharm

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.SEP = ','
        self.NULL = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        sb = []
        self.serializeHelper(root, sb)
        return ''.join(sb)

    def serializeHelper(self, root, sb):
        if root == None:
            # have to separare the 2 append, as append method doesn't return
            # the list itself; it modifies the list in place and returns None.
            sb.append(self.NULL)
            sb.append(self.SEP)
            return

        # pre-order position
        sb.append(str(root.val))
        sb.append(self.SEP)

        self.serializeHelper(root.left, sb)
        self.serializeHelper(root.right, sb)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # convert the string into a list using split(',')
        nodes = data.split(self.SEP)
        return self.deserializeHelper(nodes)

    def deserializeHelper(self, nodes: list):
        # 列表中有空指针，所以 先确定根节点，然后遵循前序遍历的规则，递归生成左右子树
        if not nodes:
            return None
        # pre-order position
        val = nodes.pop(0)
        if val == self.NULL:
            return None
        root = TreeNode(int(val))
        # below recursion calls: each call processes the next element in the
        # nodes list
        root.left = self.deserializeHelper(nodes)
        root.right = self.deserializeHelper(nodes)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
