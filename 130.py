# -*- coding = utf-8 -*-
# @Time : 1/29/2024 3:36 PM
# @Author : Lauren
# @File : 130.py
# @Software : PyCharm


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return

        height = len(board)
        length = len(board[0])

        # give dummy a spot at m*n
        myUF = UF(length * height + 1)
        dummy = length * height

        # connect dummy with the 0s in the first and last column
        for i in range(height):
            if board[i][0] == 'O':
                myUF.union(dummy, i * length + 0)
            if board[i][length - 1] == 'O':
                myUF.union(dummy, i * length + length - 1)

        # connect dummy with the 0s in the first and last row
        for i in range(length):
            if board[0][i] == 'O':
                myUF.union(dummy, 0 * length + i)
            if board[height - 1][i] == 'O':
                myUF.union(dummy, (height - 1) * length + i)

        # direction array is the oftenly used in searching up down left right
        d = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        # connect 0's with its surrounding 0s
        for i in range(height - 1):
            for j in range(length - 1):
                if board[i][j] == 'O':
                    for k in range(4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == 'O':
                            myUF.union(x * length + y, i * length + j)

        # replace all 0s which are not connected with dummy with x
        for i in range(height - 1):
            for j in range(length - 1):
                if not myUF.connected(dummy, i * length + j):
                    board[i][j] = 'X'

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

