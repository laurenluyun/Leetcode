# -*- coding = utf-8 -*-
# @Time : 1/29/2024 3:27 PM
# @Author : Lauren
# @File : 323.py
# @Software : PyCharm

# Number of Connected Components in an Undirected Graph
'''
给你输⼊⼀个包含 n 个节点的图，⽤⼀个整数 n 和⼀个数组 edges 表示，其中 edges[i] = [ai, bi] 表
示图中节点 ai 和 bi 之间有⼀条边。请你计算这幅图的连通分量个数。
'''
class Solution:
    def countComponents(self, n, edges):
        myUF = UF(n)
        # connect all the nodes
        for each in edges:
            myUF.union(each[0], each[1])
        return myUF.count()

# time complexity: O(1)
class UF:
    # n is the total number of nodes in the graph
    def __init__(self, n):
        self.count = n
        # list to store the parent node for each element
        self.parent = []
        # initialize the list: each node as its own parent node
        for i in range(n):
            self.parent.append(i)

    # return the root node of node x
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # connect p and q, in order to connect p and q, we need to connect the
    # root nodes of the 2 nodes
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        self.parent[rootP] = rootQ
        self.count -= 1

    # determine if p and q is connected or not: if p and q are connected,
    # they must share the same parent node
    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

    # return the number of 连通分量
    def count(self):
        return self.count
