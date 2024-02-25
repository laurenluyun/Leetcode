# -*- coding = utf-8 -*-
# @Time : 12/21/2023 10:00 PM
# @Author : Lauren
# @File : 704.py
# @Software : PyCharm

def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1




def main():
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    nums2 = [-1]
    target2 = 2
    print(search(nums1, target1))
    print(search(nums2, target2))

if __name__ == "__main__":
    main()

