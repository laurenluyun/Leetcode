# -*- coding = utf-8 -*-
# @Time : 1/24/2024 11:03 PM
# @Author : Lauren
# @File : 785.py
# @Software : PyCharm

# DFS solution
from collections import deque


class Solution:
    def __init__(self):
        # store the result
        self.bipartite = True
        # record the color of each node, True and False as different colors
        self.color = []
        # record if the node is visited or not
        self.visited = []

    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        self.color = [False for i in range(n)]
        self.visited = [False for i in range(n)]
        # 因为图不⼀定是联通的，可能存在多个⼦图 所以要把每个节点都作为起点进⾏⼀次遍历
        # 如果发现任何⼀个⼦图不是⼆分图，整幅图都不算⼆分图
        for i in range(n):
            # if i is not visited
            if not self.visited[i]:
                self.traverse(graph, i)
        return self.bipartite

    def traverse(self, graph, i):
        # base case the graph is not a bipartite
        if not self.bipartite:
            return
        # update i as visited
        self.visited[i] = True
        # traverse all the adjacent nodes
        for each in graph[i]:
            if not self.visited[each]:
                # if the adjacent node is not visited, the color of each
                # should be different from the color of i
                self.color[each] = not self.color[i]
                self.traverse(graph, each)
            else:
                # if the adjacent node is already visited, decide if it is
                # a bipartite by comparing the color of each and i
                if self.color[each] == self.color[i]:
                    self.bipartite = False

# BFS solution
class Solution1:
    def __init__(self):
        # store the result
        self.bipartite = True
        # record the color of each node, True and False as different colors
        self.color = []
        # record if the node is visited or not
        self.visited = []

    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        self.color = [False for i in range(n)]
        self.visited = [False for i in range(n)]
        # 因为图不⼀定是联通的，可能存在多个⼦图 所以要把每个节点都作为起点进⾏⼀次遍历
        # 如果发现任何⼀个⼦图不是⼆分图，整幅图都不算⼆分图
        for i in range(n):
            # if i is not visited
            if not self.visited[i]:
                self.bfs(graph, i)
        return self.bipartite

    def bfs(self, graph, start):
        q = deque()
        # update i as visited
        self.visited[start] = True
        q.append(start)

        while q and self.bipartite:
            v = q.popleft()
            # traverse all adjacent nodes of node v
            for each in graph[v]:
                if not self.visited[each]:
                    # if the adjacent node each has not been visited,
                    # assign a color different from node v to node each
                    self.color[each] = not self.color[v]
                    # mark node each and enque it
                    self.visited[each] = True
                    q.append(each)
                else:
                    if self.color[each] == self.color[v]:
                        self.bipartite = False
                        return


def main():
    mySolution = Solution()
    graph_1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
    graph_2 = [[1,3],[0,2],[1,3],[0,2]]
    print(mySolution.isBipartite(graph_1))
    print(mySolution.isBipartite(graph_2))

if __name__ == "__main__":
    main()

