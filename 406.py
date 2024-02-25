# -*- coding = utf-8 -*-
# @Time : 5/22/2023 5:11 PM
# @Author : Lauren
# @File : 406.py
# @Software : PyCharm
'''
Queue Reconstruction by Height
sort and insert
102ms, 16.9MB
'''

class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        output = []
        # sort the array in decreasing order of height
        # within the same height group, you would sort it in increasing order of k
        # eg: Input : [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
        # after sorting: [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
        people.sort(key = lambda x : (-x[0], x[1]))

        for each in people:
        # Now let's start the greedy here
        # We insert the entry in the output array based on the k value
        # k will act as a position within the array
            output.insert(each[1], each)

        return output


def main():
    my_solution = Solution()
    people1 = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    people2 = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    print(my_solution.reconstructQueue(people1))
    print(my_solution.reconstructQueue(people2))

if __name__ == "__main__":
    main()
