# -*- coding = utf-8 -*-
# @Time : 8/3/2023 6:34 PM
# @Author : Lauren
# @File : 1109.py Corporate Flight Bookings
'''
array of flight bookings bookings[i] = [firsti, lasti, seatsi]
represents a booking for flights first through last (inclusive)
are reserved for each flight in the range
return an array of length n as answer, answer[i] is the total number of
seats reserved for flight i
799ms, 94.63%, 30.32mb, 70.13%
'''
# @Software : PyCharm

class Difference:
    def __init__(self, arr):
        # initialize the diff array, with the 1st element assigned with
        # the 1st element of original array
        self.diff_arr = [0] * len(arr)
        self.diff_arr[0] = arr[0]
        # get the difference of the existing array, since the original array
        # consists of 0, can skip this step
        for i in range(1, len(arr)):
            self.diff_arr[i] = arr[i] - arr[i - 1]
    def increment(self, start, end, num):
        # add the num at start
        self.diff_arr[start] += num
        # if end + 1 is not out of range, decrease by num since end + 1
        if end + 1 < len(self.diff_arr):
            self.diff_arr[end + 1] -= num
    def result(self):
        res = [0] * len(self.diff_arr)
        # initialize the res array with the first element = first element
        res[0] = self.diff_arr[0]
        if len(res) > 1:
            # update the res array by adding the diff value to the re array
            for index in range(len(res)):
                res[index] = res[index - 1] + self.diff_arr[index]
        return res


class Solution:

    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> \
            list[int]:
        arr = [0] * n
        myDifference = Difference(arr)
        for booking in bookings:
            start = booking[0] - 1
            end = booking[1] - 1
            num = booking[2]
            myDifference.increment(start, end, num)
        return myDifference.result()


def main():
    mySolution = Solution()
    bookings1 = [[1,2,10],[2,3,20],[2,5,25]]
    n1 = 5
    bookings2 = [[1,2,10],[2,2,15]]
    n2 = 2
    bookings3 = [[1, 1, 10]]
    n3 = 1
    print(mySolution.corpFlightBookings(bookings1,n1))
    print(mySolution.corpFlightBookings(bookings2,n2))
    print(mySolution.corpFlightBookings(bookings3,n3))

if __name__ == "__main__":
    main()


