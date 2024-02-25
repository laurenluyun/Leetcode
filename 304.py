# -*- coding = utf-8 -*-
# @Time : 8/2/2023 12:06 PM
# @Author : Lauren
# @File : 304.py Range Sum Query 2D - Immutable Medium
# O(n) to get the prefix array - calculate the sum of the square for every
# position of the matrix  list comprehension, also needs to add extra col and
# row all with value 0 for 303: prefixSum[i + 1] = nums[0,...i], for 304:
# prefixSum[r + 1][c + 1] = sum of the value of the space with left up
# corner [0, 0], bottom right corner[r, c]
# @Software : PyCharm

class NumMatrix:
    '''
    1118ms, 98.28%, 27.02mb, 55.17%
    '''
    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # list comprehension to create the prefixDum matrix which is one
        # unit larger than the original matrix
        self.prefixSum = [[0] * (COLS + 1) for r in range(ROWS + 1)]
        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix += matrix[row][col]
                above = self.prefixSum[row][col + 1]
                # we hava to increment the index by 1 because the first row
                # and the first column and first row are all gonna be 0
                self.prefixSum[row + 1][col + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        prefix sum: we are going to calculate the sum of (0,0,r, c) for each
        position of the matrix and store it in the bottom right value.
        Specifically, the prefix sum = the sum of the same row + the sum of the
        rows above.NOTE: since for the space in the first row, to give the
        row above the first row will return error, we will add a row as the first row
        with value of 0, to make it symetry we can also add a col of cells
        with value 0 => the matrix we use has larger index for the same
        position by 1 prefix[r + 1][c + 1] = sum of row r as of column c in
        the matrix + prefix[r][c+1]
        Next, to get the required sum [r1, c1, r2, c2], we can firstly get
        the total sum at position [r2, c2] prefix[r2 + 1][c2 + 1] deducted by
        1. sum at position[r2, c1 - 1] prefix[r2+1, c1]
        2. sum at position [r1 - 1, c2] prefix [r1, c2 + 1]
        add back sum at position [r1 - 1, c1 -1] prefix [r1, c1]
        '''
        return self.prefixSum[row2 + 1][col2 + 1] - self.prefixSum[row2 +
                                                                   1][col1]\
               -self.prefixSum[row1][col2 + 1] + self.prefixSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)