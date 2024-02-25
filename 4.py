# -*- coding = utf-8 -*-
# @Time : 12/22/2023 7:19 PM
# @Author : Lauren
# @File : 4.py
# @Software : PyCharm

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) ->\
            float:
        # pick the shorter list as A to do the binary search
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2
        left, right = 0, len(A) - 1
        while True:
            mid = (left + right) // 2
            bEnd = half - (mid + 1) - 1
            # resolve the edge cases
            aMid_value = A[mid] if mid >= 0 else float("-infinity")
            aMidRight_value = A[mid + 1] if (mid + 1) < len(A) else float(
                "infinity")
            bEnd_value = B[bEnd] if bEnd >= 0 else float("-infinity")
            bEndRight_value = B[bEnd + 1] if (bEnd + 1) < len(B) else \
                float("infinity")
            # if partition is correct
            if aMid_value <= bEndRight_value and bEnd_value <= \
                    aMidRight_value:
                if total % 2: #odd number of elements
                    return min(aMidRight_value, bEndRight_value)
                else:
                    return (max(aMid_value, bEnd_value) + min(
                        aMidRight_value, bEndRight_value)) / 2
            # shrink the right side to decrease aMid
            elif aMid_value > bEndRight_value:
                right = mid - 1
            # shrink the left side to increase aMid
            else:
                left = mid + 1



def main():
    mySolution = Solution()
    nums1 = [1, 3]
    nums2 = [2]

    nums3 = [1, 2]
    nums4 = [3, 4]

    print(mySolution.findMedianSortedArrays(nums1, nums2))
    print(mySolution.findMedianSortedArrays(nums3, nums4))

if __name__ == "__main__":
    main()
