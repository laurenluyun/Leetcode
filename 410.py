# -*- coding = utf-8 -*-
# @Time : 12/22/2023 5:52 PM
# @Author : Lauren
# @File : 410.py
# @Software : PyCharm

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # greedy algo to determine if we can split the nums into subarrays
        # whose maxim sum < largest
        def canSplit(largest):
            subarray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n
            return subarray + 1 <= k

        # binary search to ge the minimum sum
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = left + (right - left) // 2
            # the maximum sum can be smaller
            if canSplit(mid):
                right = mid - 1
            # the maximum sum should be larger
            else:
                left = mid + 1
        return left


def main():
    mySolution = Solution()
    nums1 = [7, 2, 5, 10, 8]
    k1 = 2

    nums2 = [1, 2, 3, 4, 5]
    k2 = 2

    print(mySolution.splitArray(nums1, k1))
    print(mySolution.splitArray(nums2, k2))

if __name__ == "__main__":
    main()
