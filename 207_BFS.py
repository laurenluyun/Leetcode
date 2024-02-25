# -*- coding = utf-8 -*-
# @Time : 1/24/2024 8:02 PM
# @Author : Lauren
# @File : 207_BFS.py
# @Software : PyCharm

'''
环检测BFS
'''
from collections import deque

class Solution:
    '''
    convert the given info into a graph: adjacency list
    '''
    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]
        for each in prerequisites:
            # node each[1], pointing to each[0], indicating the former is
            # prerequisite, one root can point to multiple different nodes,
            # so append
            graph[each[1]].append(each[0])
        return graph

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) ->\
            bool:
        graph = self.buildGraph(numCourses, prerequisites)
        indegree = [0 for i in range(numCourses)]
        for edge in prerequisites:
            fromm = edge[1]
            to = edge[0]
            # because we are record the indegree, update the indegree for to
            indegree[to] += 1

        q = deque()
        for i in range(numCourses):
            # 节点i没有入度，即没有依赖的节点，可以作为拓扑排序的起点，加入队列, 开始进行BFS
            # 减少其相关的节点的indegree
            if indegree[i] == 0:
                q.append(i)

        # record the number of nodes that has been traversed
        count = 0
        # start the BFS loop while the q is not empty, the while loop
        # terminates when there are no more nodes with an indegree of 0
        # available for processing
        while q:
            # pop out the node cur and then decrease the indegree of the
            # nodes cur points to
            cur = q.popleft()
            count += 1
            for next in graph[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    # if the indegree = 0,next依赖的节点都已经被遍历,加入que
                    q.append(next)

        # if all the nodes have been traversed, there is no cycle
        return count == numCourses

def main():
    mySolution = Solution()
    numCourses_1 = 2
    prerequisites_1 = [[1, 0]]
    numCourses_2 = 2
    prerequisites_2 = [[1, 0], [0, 1]]
    print(mySolution.canFinish(numCourses_1, prerequisites_1))
    print(mySolution.canFinish(numCourses_2, prerequisites_2))

if __name__ == "__main__":
    main()

