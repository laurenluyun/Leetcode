# -*- coding = utf-8 -*-
# @Time : 1/24/2024 9:03 PM
# @Author : Lauren
# @File : topological sort_BFS.py
# @Software : PyCharm

'''
只要图中⽆环，那么我们就用BFS记录下进入deque的节点，就是拓扑排序
'''
from collections import deque

class Solution:

    def buildGraph(self, numCourses, prerequisites):
        '''
        build the adjacency list
        '''
        graph = [[] for i in range(numCourses)]
        for each in prerequisites:
            graph[each[1]].append(each[0])
        return graph

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) ->\
            list[int]:
        graph = self.buildGraph(numCourses, prerequisites)
        indegree = [0 for i in range(numCourses)]
        # initiate the indegree list to record the indegree number for each
        # node
        for edge in prerequisites:
            from_node = edge[1]
            to_node = edge[0]
            indegree[to_node] += 1

        q = deque()
        res = []
        # initialize the q with nodes with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            cur = q.popleft()
            count += 1
            # record the res
            res.append(cur)
            # BFS
            for next in graph[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)

        if count == numCourses:
            return res
        else:
            return []

def main():
    mySolution = Solution()
    numCourses_1 = 2
    prerequisites_1 = [[1, 0]]
    numCourses_2 = 4
    prerequisites_2 = [[1,0],[2,0],[3,1],[3,2]]
    numCourses_3 = 1
    prerequisites_3 = []
    print(mySolution.findOrder(numCourses_1, prerequisites_1))
    print(mySolution.findOrder(numCourses_2, prerequisites_2))
    print(mySolution.findOrder(numCourses_3, prerequisites_3))

if __name__ == "__main__":
    main()
