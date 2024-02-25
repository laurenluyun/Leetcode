# -*- coding = utf-8 -*-
# @Time : 1/23/2024 10:27 PM
# @Author : Lauren
# @File : 210.py
# @Software : PyCharm

'''
只要图中⽆环，那么我们就调⽤ traverse 函数对图进⾏
DFS 遍历，记录后序遍历结果，最后把后序遍历结果反转，即为拓扑排序，作为最终的答案。
'''
class Solution:
    def __init__(self):
        self.visited= []
        self.onPath = []
        self.postOrder = []
        self.hasCycle = False

    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]
        for each in prerequisites:
            graph[each[1]].append(each[0])
        return graph

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) ->\
            list[int]:
        if numCourses == 1:
            return [0]
        self.onPath = [0 for i in range(numCourses)]
        self.visited = [0 for i in range(numCourses)]
        graph = self.buildGraph(numCourses, prerequisites)
        # traverse each node to call the recursive function
        for i in range(numCourses):
            self.traverse(graph, i)

        # return empty array if there's cycle in the graph
        if self.hasCycle:
            return []
        # else reverse the post-order res
        self.postOrder.reverse()
        # do not forget to do the slicing
        return self.postOrder[:numCourses]

    def traverse(self, graph, s):
        # pre-order
        if self.onPath[s]:
            self.hasCycle = True
        if self.visited[s] or self.hasCycle:
            return
        self.visited[s] = True
        self.onPath[s] = True
        # recursion
        for each in graph[s]:
            self.traverse(graph, each)

        # post-order
        self.onPath[s] = False
        # store the root node in the list in post-order traversal order
        self.postOrder.append(s)


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
