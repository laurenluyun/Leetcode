# -*- coding = utf-8 -*-
# @Time : 1/28/2024 2:05 PM
# @Author : Lauren
# @File : 886.py
# @Software : PyCharm

class Solution:
    def __init__(self):
        self.isOK = True
        self.visited = []
        self.color = []

    def buildGraph(self, n, dislikes):
        '''
        build the adjacency list
        '''
        graph = [[] for i in range(n)]
        for each in dislikes:
            # 无向图 相当于 双向图
            graph[each[0]- 1].append(each[1] - 1)
            graph[each[1] - 1].append(each[0] - 1)
        return graph

    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph = self.buildGraph(n, dislikes)
        self.visited = [False for i in range(n)]
        self.color = [False for i in range(n)]
        for i in range(n):
            if not self.visited[i]:
                self.traverse(graph, i)
        return self.isOK

    def traverse(self, graph, i):
        if not self.isOK:
            return
        self.visited[i] = True
        for each in graph[i]:
            if self.visited[each]:
                if self.color[each] == self.color[i]:
                    self.isOK = False
            else:
                self.color[each] = not self.color[i]
                self.traverse(graph, each)

def main():
    mySolution = Solution()
    graph_1 = [[1,2],[1,3],[2,4]]
    n_1 = 4
    n_2 = 3
    graph_2 = [[1,2],[1,3],[2,3]]
    print(mySolution.possibleBipartition(n_1, graph_1))
    print(mySolution.possibleBipartition(n_2, graph_2))

if __name__ == "__main__":
    main()
