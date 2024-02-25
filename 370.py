# -*- coding = utf-8 -*-
# @Time : 8/3/2023 5:57 PM
# @Author : Lauren
# @File : 370.py Range Addition diff
'''
will be given a list of n * [0]
and k operations
each operation is denoted as [startIndex, endIndex, inc]
return the list after k operations
e.g.
length = 5, updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
1st: [0, 2, 2, 2, 0]
2nd: [0, 2, 5, 5, 3]
3rd: [-2, 0, 3, 5, 3]
output = [-2, 0, 3, 5, 3]
'''
# @Software : PyCharm

class Solution:

    def Difference(self, arr, start, end, num):

        # initialize the diff array, with the 1st element assigned with
        # the 1st element of original array
        diff_arr = [0] * len(arr)
        # since the first element of arr is 0, can skip this step
        diff_arr[0] = arr[0]
        # get the difference of the existing array, since the original array
        # consists of 0, can skip this step
        for i in range(1, len(arr)):
            diff_arr[i] = arr[i] - arr[i - 1]
        # add the num at start
        diff_arr[start] += num
        # if end + 1 is not out of range, decrease by num since end + 1
        if end + 1 < len(diff_arr):
            diff_arr[end + 1] -= num
        # initialize the res array with the first element = first element
        # of arr
        res = [0] * len(arr)
        # since the first element of arr is 0, can skip this step
        res[0] = arr[0]
        # update the res array by adding the diff value to the re array
        for index in range(len(arr)):
            res[index] = res[index - 1] + diff_arr[index]
        return res

    def getMidifiedArray(self,length, updates):
        arr = [0] * length
        for update in updates:
            start = update[0]
            end = update[1]
            num = update[2]
            arr = self.Difference(arr, start, end, num)


        return arr












