# -*- coding = utf-8 -*-
# @Time : 1/31/2024 9:24 PM
# @Author : Lauren
# @File : BFS_Graph_traversal.py
# @Software : PyCharm
def BFS(start):
    # main data structure, queue
    q = []
    # to avoid circle
    visited = set()
    q.append(start)
    visited.add(start)
    while q:
        sz = len(q)
        step = 0


        for i in range(sz):
            curr = q.pop()
            print(f"the smallest distance from {from, }")
            if visited






