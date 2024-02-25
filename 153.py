# -*- coding = utf-8 -*-
# @Time : 7/22/2023 12:28 PM
# @Author : Lauren
# @File : 153.py Find Minimum in Rotated Sorted Array
# Medium Binary Search You must write an algorithm that runs in O(log n) time.
# @Software : PyCharm
# 58ms, 47.62%, 16.76mb, 12.57%
def findMin(nums: list[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1
    while l <= r:
        # if the array is already sorted, take the left most value
        if nums[l] < nums[r]:
            res = min(res,nums[l])
        # if the array is rotated
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res

def findMin2(nums: list[int]) -> int:
    res = nums[0]
    left = 0
    right = len(nums) - 1
    while left <= right:
        # check
        if nums[left] < nums[right]:
            res = min(res, nums[left])
        mid = left + (right - left) // 2
        res = min(res, nums[mid]) # check the mid first
        if nums[mid] >= nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid - 1
    return res


def main():
    nums_1 = [3, 4, 5, 1, 2]
    nums_2 = [4,5,6,7,0,1,2]
    nums_3 = [11,13,15,17]
    nums_4 = [3, 1, 2]
    nums_5 = [2, 1]
    print(findMin2(nums_1))
    print(findMin2(nums_2))
    print(findMin2(nums_3))
    print(findMin2(nums_4))
    print(findMin2(nums_5))

if __name__ == "__main__":
    main()
