# -*- coding = utf-8 -*-
# @Time : 1/31/2024 5:37 PM
# @Author : Lauren
# @File : Prim.py
# @Software : PyCharm
import heapq


class Prim:
    def __init__(self):
        # priority queue to store the cut edges[[weight, from, to][weight, from, to]]
        self.pq = []
        # record if specific node has been included in the MST
        self.inMST = []
        # record the weights of the MST
        self.weightSum = 0
        # adjacency list of the graph - nested list
        # [ [[from, to, weight],[from, to, weight],..] 0
        #   [[from, to, weight],[from, to, weight],..] 1
        #   ...
        #   [[from, to, weight],[from, to, weight],..] ] n
        self.graph = []

    def Prim(self, graph):
        self.graph = graph
        self.inMST = [False for i in range(len(graph))]
        # cut from node 0
        self.inMST[0] = True
        self.cut(0)
        # keep cutting, add the edge into the MST
        while self.pq:
            edge = heapq.heappop(self.pq)
            to, weight = edge[2], edge[0]
            # node to is already in the MST, so skip the node
            if self.inMST[to]:
                continue
            self.weightSum += weight
            self.inMST[to] = True
            # new round of cutting the newly added node
            self.cut(to)

    # add the cutting edge into the pq
    def cut(self, s):
        # traverse all the adjacent edges of the node s， add those which is
        # not already in the MST
        for edge in self.graph[s]:
            to = edge[1]
            # avoid duplicated edges
            if self.inMST[to]:
                # node to is already in the MST, so skip the node
                continue
            # To ensure the heap is arranged according to the weight,
            # we can negate the weights when adding them to the heap.
            # This way, the smallest weight will have the largest negated
            # value and will be popped out first.
            heapq.heappush(self.pq, [edge[2], edge[0],edge[1]])

    def weight_sum(self):
        return self.weightSum

    '''
    all() function in Python returns True if all elements of the iterable 
    (in this case, the list self.inMST) are true, and it returns False if any 
    element is false. It is used for checking whether all elements in the 
    list are True
    '''
    def all_connected(self):
        return all(self.inMST)

