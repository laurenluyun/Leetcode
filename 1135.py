# -*- coding = utf-8 -*-
# @Time : 1/31/2024 6:34 PM
# @Author : Lauren
# @File : 1135.py
# @Software : PyCharm
import heapq

class Solution:
    def minimumCost(self, n, connections):
        graph = self.buildGraph(n, connections)
        myPrim = Prim(graph)
        if not myPrim.all_connected():
            return -1
        return myPrim.weightSum

    def buildGraph(self, n, connections):
        graph = [[] for i in range(n)]
        for conn in connections:
            u = conn[0] - 1
            v = conn[1] - 1
            weight = conn[2]
            # 无向图就是双向图，edge is represented as [from, to, weight]
            graph[u].append([u, v, weight])
            graph[v].append([v, u, weight])
        return graph

class Prim:
    def __init__(self, graph):
        # [ [[from, to, weight],[from, to, weight],..]
        #   [[from, to, weight],[from, to, weight],..]
        #   ...
        #   [[from, to, weight],[from, to, weight],..] ]
        self.graph = graph
        # priority queue min-heap to store the cut edges[[weight, from,
        # to][weight,
        # from, to]]
        self.pq = []
        self.inMST = []
        self.weightSum = 0


    def Prim(self):
        self.inMST = [False for i in range(len(self.graph))]
        self.Cut(0)
        self.inMST[0] = True
        while self.pq:
            edge = heapq.heappop(self.pq)
            to, weight = edge[2], edge[0]
            if self.inMST[to]:
                continue
            self.weightSum += weight
            self.inMST[to] = True
            self.Cut(to)

    # cut the adjacent edge of node s
    def Cut(self, s):
        for edge in self.graph[s]:
            to = edge[1]
            if self.inMST[to]:
                continue
            heapq.heappush(self.pq, [edge[2], edge[0], edge[1]])

    def all_connected(self):
        return all(self.inMST)


