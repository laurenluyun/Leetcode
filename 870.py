# -*- coding = utf-8 -*-
# @Time : 12/24/2023 12:48 AM
# @Author : Lauren
# @File : 870.py
# @Software : PyCharm

class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()  # Sort nums1 in ascending order
        # Using enumerate to keep track of the original indices of nums2 elements.
        # creating a list of tuples, where each tuple contains an index and a
        # value from nums2, and then sorting these tuples based on the values in descending order.
        # key=lambda x: x[1]: This specifies that the sorting should be based on the second element of each tuple (the values from nums2).
        nums2_ordered = sorted(enumerate(nums2), key=lambda x: x[1],
                               reverse=True)

        res = [0] * len(nums1)
        left, right = 0, len(nums1) - 1

        # i will be the loop index, and (index, value) will be a tuple
        # containing an index and a value from nums2, sorted in descending order.
        # This loop is useful for processing the elements of nums2_ordered in a specific order while having access to both the index and value of each element.
        for i, (index, value) in enumerate(nums2_ordered):
            if nums1[right] > value:
                res[index] = nums1[right]
                right -= 1
            else:
                res[index] = nums1[left]
                left += 1

        return res





def main():
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    nums3 = [12, 24, 8, 32]
    nums4 = [13, 25, 32, 11]
    mySolution = Solution()
    print(mySolution.advantageCount(nums1, nums2))
    print(mySolution.advantageCount(nums3, nums4))

if __name__ == "__main__":
    main()
