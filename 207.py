# -*- coding = utf-8 -*-
# @Time : 1/21/2024 5:28 PM
# @Author : Lauren
# @File : 207.py
# @Software : PyCharm
'''
环检测DFS
题⽬应该不难理解，什么时候⽆法修完所有课程？当存在循环依赖的时候。
我们⾸先可以把课程看成「有向图」中的节点，节点编号分别是 0, 1, ..., numCourses1，
把课程之间的依赖关系看做节点之间的有向边。⽐如说必须修完课程 1 才能去修课程 3，
那么就有⼀条有向边从节点 1 指向 3。
如果发现这幅有向图中存在环，那就说明课程之间存在循环依赖，肯定没办法全部上完；反之，如果没有
环，那么肯定能上完全部课程。
'''

class Solution:
    '''
    graph[s] 是⼀个列表，存储着节点 s 所指向的节点。
    '''
    def __init__(self):
        # cycle detection within a single DFS traversal, as it will exit at
        # the end of a single DFS traversal
        self.onPath = []
        # record visited nodes, this is important to avoid unnecessary
        # re-traversal of nodes across multiple DFS traversals
        self.visited = []
        self.hasCycle = False

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

    '''
    initiates DFS traversal for all the nodes of the graph and call 
    the recursive function that marks nodes as visited and checks for cycles 
    during the traversal.
    '''
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) ->\
            bool:
        graph = self.buildGraph(numCourses, prerequisites)
        # create a list of boolean with initialized value of False
        self.visited = [0 for i in range(numCourses)]
        # create a list of boolean with initialized value of False
        self.onPath = [0 for i in range(numCourses)]
        for i in range(numCourses):
            # traverse all the nodes of the graph, since not every node is
            # connected in the graph, we need a for loop beginning at
            # each node to call a DFS
            self.traverse(graph, i)
        # if the graph has a cycle return False, otherwise return True
        return not self.hasCycle

    '''
    recursion to traverse the tree
    '''
    def traverse(self, graph, s):
        # if s is already on path, there is cycle, update the hasCycle
        if self.onPath[s]:
            self.hasCycle = True
        # if s is already visited or the path has cycle, return
        if self.visited[s] or self.hasCycle:
            return
        # pre order position, update the current node as visited and onPath
        self.visited[s] = True
        self.onPath[s] = True
        # recursion
        for each in graph[s]:
            self.traverse(graph, each)
        # post order position, get the current node out of the path
        self.onPath[s] = False

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







