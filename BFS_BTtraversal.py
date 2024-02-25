# -*- coding = utf-8 -*-
# @Time : 1/31/2024 8:49 PM
# @Author : Lauren
# @File : BFS_BTtraversal.py
# @Software : PyCharm
from collections import deque


def level_traverse(root):
    if root == None:
        return 0
    # double queue
    q = deque(root)
    depth = 1
    while q:
        sz = len(q)
        for i in range(sz):
            curr = q.popleft()
            print(f"node {curr.val} is at level {depth}")
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        depth += 1

