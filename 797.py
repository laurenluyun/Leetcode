# -*- coding = utf-8 -*-
# @Time : 1/17/2024 1:25 AM
# @Author : Lauren
# @File : 797.py
# @Software : PyCharm

'''
解法很简单，以 0 为起点遍历图，同时记录遍历过的路径，当遍历到终点时将路径记录下来即可。
然输⼊的图是⽆环的，我们就不需要 visited 数组辅助
'''
class Solution:
    def __init__(self):
        self.res = []

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # main the path
        path = []
        # the graph always starts from node 0
        self.traverse(graph, 0, path)
        return self.res

    def traverse(self, graph, s, path):
        # add node s to path
        path.append(s)
        n = len(graph)
        if s == n - 1:
            # reaches the end
            # NOTE: why do we use copy: By creating a copy of the path
            # using path.copy(), you ensure that each recursive call has its
            # own independent copy of the path. This way, when backtracking
            # occurs (removing the last element), it only affects the
            # current copy, leaving previous copies unchanged.
            # as path is mutable and can be changed any time, it is pass by
            # reference
            self.res.append(path.copy())
        # recursion for the adjacent nodes
        for each in graph[s]:
            self.traverse(graph, each, path)
        # remove s from the path
        path.pop()

def main():
    mySolution = Solution()
    graph_1 = [[1,2],[3],[3],[]]
    graph_2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(mySolution.allPathsSourceTarget(graph_1))
    print(mySolution.allPathsSourceTarget(graph_2))

if __name__ == "__main__":
    main()

