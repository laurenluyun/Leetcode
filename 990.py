# -*- coding = utf-8 -*-
# @Time : 1/29/2024 4:44 PM
# @Author : Lauren
# @File : 990.py
# @Software : PyCharm

class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        myUF = UF(26)
        # connet those letters with ==
        for each in equations:
            if each[1] == '=':
                x = each[0]
                y = each[3]
                myUF.union(ord(x) - ord('a'), ord(y) - ord('a'))
        for each in equations:
            if each[1] == '!':
                x = each[0]
                y = each[3]
                if myUF.connected(ord(x) - ord('a'), ord(y) - ord('a')):
                    return False
        return True

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
