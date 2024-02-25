# -*- coding = utf-8 -*-
# @Time : 5/19/2023 11:57 AM
# @Author : Lauren
# @File : 452.py
# @Software : PyCharm
'''
Greedy Strategy
Minimum Number of Arrows to Burst Balloons
'''

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        count = 1
        vertical = points[0][1]
        for index in range(1, len(points)):
            if points[index][0] > points[index - 1][1]:
                count += 1
            elif points[index][0] <= points[index - 1][1] and vertical < \
                    points[index][0]:
                count += 1
                vertical = points[index][1]
            else:
                vertical = min(vertical, points[index][1], points[index -
                                                                 1][1])
        return count

class Solution1:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # sort by the second element
        points.sort(key = lambda x: x[1])
        tally, bow = 1, points[0][1]
        for start, end in points:
            if bow < start:
                bow = end
                tally += 1
        return tally




def main():
    my_solution = Solution1()
    points1 = [[10,16],[2,8],[1,6],[7,12]]
    points2 = [[1,2],[3,4],[5,6],[7,8]]
    points3 = [[1,2],[2,3],[3,4],[4,5]]
    print(my_solution.findMinArrowShots(points1))
    print(my_solution.findMinArrowShots(points2))
    print(my_solution.findMinArrowShots(points3))

if __name__ == "__main__":
    main()