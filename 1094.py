# -*- coding = utf-8 -*-
# @Time : 8/4/2023 4:06 PM
# @Author : Lauren 
# @File : 1094.py CAR POOLING MEIDUM
# trips[i] = [numPassengersi, fromi, toi] i 0 <= fromi < toi <= 1000 trips[i].length == 3
# meaning we can have maximum 1001 stations
'''
len(length) = 1001 the number of customers at each point of the arr should
be <= capacity
use diff to calculate the number of customers at each station => res
compare each element in the res with the capacity
85ms, 16.92mb
'''
# @Software : PyCharm

class Difference:
    def __init__(self, arr):
        self.arr_diff = [0] * len(arr)
        self.arr_diff[0] = arr[0]
        for i in range(1, len(arr)):
            self.arr_diff[i] = arr[i] - arr[i - 1]

    def increment(self, fro, to, numPassengers):
        self.arr_diff[fro] += numPassengers
        if to < len(self.arr_diff):
            self.arr_diff[to] -= numPassengers
    def result(self):
        res = [0] * len(self.arr_diff)
        res[0] = self.arr_diff[0]
        if len(res) > 1:
            for index in range(1, len(res)):
                res[index] = res[index - 1] + self.arr_diff[index]
        return res

class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        arr = [0] * 1001
        myDifference = Difference(arr)
        for trip in trips:
            numPassengers = trip[0]
            fro = trip[1]
            to = trip[2]
            myDifference.increment(fro, to, numPassengers)
        result = myDifference.result()
        return max(result) <= capacity



def main():
    mySolution = Solution()
    trips1 = [[2,1,5],[3,3,7]]
    capacity1 = 4
    trips2 = [[2,1,5],[3,3,7]]
    capacity2 = 5
    trips3 = [[2, 1, 5], [3, 5, 7]]
    capacity3 = 3
    print(mySolution.carPooling(trips1, capacity1))
    print(mySolution.carPooling(trips2, capacity2))
    print(mySolution.carPooling(trips3, capacity3))

if __name__ == "__main__":
    main()



