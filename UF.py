# -*- coding = utf-8 -*-
# @Time : 1/28/2024 11:49 PM
# @Author : Lauren
# @File : UF.py
# @Software : PyCharm

# time complexity: n
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
        while self.parent[x] != x:
            root = self.parent[x]
        return root

    # connect p and q, in order to connect p and q, we need to connect the
    # root nodes of the 2 nodes, i.e. make one of the root node the parent
    # node of the other root node
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


# time complexity: lgn
class UF1:
    # n is the total number of nodes in the graph
    def __init__(self, n):
        self.count = n
        self.size = []
        # list to store the parent node for each element
        self.parent = []
        # initialize the list: each node as its own parent node, weight is 1
        for i in range(n):
            self.parent.append(i)
            self.size.append(1)

    # return the root node of node x
    def find(self, x):
        while self.parent[x] != x:
            root = self.parent[x]
        return root

    # connect p and q, in order to connect p and q, we need to connect the
    # root nodes of the 2 nodes, i.e. make one of the root node the parent
    # node of the other root node
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        # small tree is connected under a big tree
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
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

# time complexity: O(1)
class UF2:
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
        while self.parent[x] != x:
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
