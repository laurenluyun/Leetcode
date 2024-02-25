# -*- coding = utf-8 -*-
# @Time : 5/17/2023 3:29 PM
# @Author : Lauren
# @File : 435.py
# @Software : PyCharm

'''
non-overlapping intervals
Given an array of intervals where intervals[i] = [starti, endi], return the
minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.
greedy algo, choose the interval with the smaller end number
1. sort the list by the value of the end number of each element
2. choose the next interval with the smallest end number and not having
overlap
1405ms 55.2mb
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        endList = []
        for each in intervals:
            endList.append(each[1])
        # get the end number sorted in non-descending order
        sor = sorted(endList)
        # get the sorted list in the same order as sor
        sortedList = []
        for each in sor:
            for element in intervals:
                if each == element[1]:
                    sortedList.append(element)
                    intervals.remove(element)

        removeCount = 0
        length = len(sortedList)
        i = 1
        while i < length:
            if sortedList[i][0] < sortedList[i - 1][1]:
                removeCount += 1
                sortedList.pop(i)
                length -= 1
            else:
                i += 1

        return removeCount

class Solution1:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sorting the intervals in ascending order w.r.t. the lower bounds.
        # This requires O(nlogn)
        intervals.sort()
        # init result: keeps track of the count of overlapping intervals
        # prev acts as the initial lower bound value
        result, prev = 0, intervals[0][1]
        # l is the lower bound, r is the upper bound
        # iterate through each element of intervals
        for l, r in intervals[1:]:
            # if the lower bound is smaller than prev upper bound overlap + 1
            if l < prev:
                result += 1
                if r > prev:
                    # if this condition satisfies, skip updating the prev
                    continue
            # reset the previous upper bound to be the current upper bound
            prev = r
        return result

def main():
    my_solution = Solution1()
    intervals1 = [[1,2],[2,3],[3,4],[1,3]]
    intervals2 = [[1,2],[1,2],[1,2]]
    intervals3 = [[1,100],[11,22],[1,11],[2,12]]
    print(my_solution.eraseOverlapIntervals(intervals1))
    print(my_solution.eraseOverlapIntervals(intervals2))
    print(my_solution.eraseOverlapIntervals(intervals3))

if __name__ == "__main__":
    main()