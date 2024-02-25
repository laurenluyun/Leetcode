# -*- coding = utf-8 -*-
# @Time : 5/25/2023 12:02 PM
# @Author : Lauren
# @File : 88.py
# @Software : PyCharm
'''
Merge and sorted Array (Easy)
Two Pointers
NOte: The two list are already sorted in non-descending order, so when
comparing from the right to left, the bigger one should be pushed to the
back of the list A
50ms, 16.4mb
'''

class Solution:
    def merge(self, A: list[int], m: int, B: list[int], n: int) -> \
            None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # a: 1st pointer which starts from the last non-zero element of A,
        # forwarding to the start of A
        # b: 2nd pointer which starts from the end of B, forwarding to the
        # start of B
        # write_index: 3rd pointer which starts from the end of A, forwarding
        # to the start of A, to be used as the index to store the larger
        # number after comparison
        a, b, write_index = m - 1, n - 1, m + n - 1

        # while loop when b >= 0
        while b >= 0:
            # if the 1st pointer has not reached the start of List A
            # and the current element of A is greater than the repective
            # element of list B
            # whichever is larger is added to the back of list A at index
            # write_index
            if a >= 0 and A[a] > B[b]:
                A[write_index] = A[a]
                # update a to the next comparison
                a -= 1
            else:
                A[write_index] = B[b]
                b -= 1

            write_index -= 1
        return A


def main():
    mySolution = Solution()
    A1 = [1,2,3,0,0,0]
    m1 = 3
    B1 = [2,5,6]
    n1 = 3

    A2 = [1]
    m2 = 1
    B2 = []
    n2 = 0

    A3 = [0]
    m3 = 0
    B3 = [1]
    n3 = 1
    print(mySolution.merge(A1, m1, B1, n1))
    print(mySolution.merge(A2, m2, B2, n2))
    print(mySolution.merge(A3, m3, B3, n3))

if __name__ == "__main__":
    main()
