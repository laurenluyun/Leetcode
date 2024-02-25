# -*- coding = utf-8 -*-
# @Time : 1/29/2024 5:29 PM
# @Author : Lauren
# @File : 1584.py
# @Software : PyCharm
import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        # generate all the edges and weights
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]
                # use i, j to represent the edges
                edges.append([i, j, abs(xi - xj) + abs(yi - yj)])
        # sort the edges in ascending order by the weight
        edges.sort(key=lambda x : x[2])
        # call krustal
        mst = 0
        myUF =UF(n)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            weight = edge[2]
            # if there is circle, cannot add into the mst
            if myUF.connected(u, v):
                continue
            # if no circle, then add to the mst
            mst += weight
            myUF.union(u, v)
        return mst


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

class Solution1:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        graph = self.buildGraph(n, points)
        myPrim = Prim(graph)
        myPrim.prim()
        return myPrim.weightSum()

    def buildGraph(self, n, points):
        graphs = [[] for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]
                # use i, j to represent the edges
                weight = abs(xi - xj) + abs(yi - yj)
                graphs[i].append([i, j, weight])
                graphs[j].append([j, i, weight])
        return graphs

class Prim:
    def __init__(self, graph):
        # a nested list of edges of nodes [ [from, to, weight], []]
        self.graph = graph
        self.inMST = [False for i in range(len(graph))]
        self.weightSum = 0
        # a list of list, each list is [weight, from, to]
        self.pq = []

    # cut from node 0 and mark it as in MST, while pq is not empty, pop out
    # the smallest edge from pq
    # in Python heapq is a min-heap
    def prim(self):
        self.cut(0)
        self.inMST[0] = True
        while self.pq:
            edge = heapq.heappop(self.pq)
            to, weight = edge[2], edge[0]
            if self.inMST[to]:
                continue
            self.weightSum += weight
            self.inMST[to] = True
            self.cut(to)

    # cut in this function means traverse all the adjacent nodes of node s,
    # if it's not in MST, then add the edge to the pq
    def cut(self, s):
        for edge in self.graph[s]:
            to = edge[1]
            if self.inMST[to]:
                continue
            # To ensure the heap is arranged according to the weight,
            # we can negate the weights when adding them to the heap.
            # This way, the smallest weight will have the largest negated
            # value and will be popped out first.
            heapq.heappush(self.pq, [edge[2], edge[0],edge[1]])

    # def weight_sum(self):
    #     return self.weightSum

    # def all_connected(self):
    #     return all(self.inMST)

