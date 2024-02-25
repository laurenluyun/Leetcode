# -*- coding = utf-8 -*-
# @Time : 6/1/2023 7:26 PM
# @Author : Lauren
# @File : 33.py
# @Software : PyCharm

'''
binary search
left, right and mid pointer
49ms 16.8mb
'''
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex <= rightIndex:
            midIndex = (leftIndex + rightIndex) // 2
            if nums[midIndex] == target:
                return midIndex

            # if the mid is in the left portion
            if nums[leftIndex] <= nums[midIndex]:
                # when the target is greater than the mid or target is less
                # than the extreme value, move the pointers to the right
                if target > nums[midIndex] or target < nums[leftIndex]:
                    leftIndex = midIndex + 1

                else:
                    # if the target is between mid and left, move the
                    # pointers to the left
                    rightIndex = midIndex - 1

            # if the mid point is in the right portion
            else:
                # if the target is less than the mid point or is greater
                # than the right most value, move the pointers to the left
                if target < nums[midIndex] or target > nums[rightIndex]:
                    rightIndex = midIndex - 1

                else:
                    # if the target is within the right and the mid,
                    # move all the pointers to the right
                    leftIndex = midIndex + 1
        return -1

class Solution1:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # compare within left side
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                #compare within the right side
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

def main():
    mySolution = Solution1()
    list1 = [4,5,6,7,0,1,2]
    target1 = 0

    list2 = [4,5,6,7,0,1,2]
    target2 = 3

    # list3 = [1, 0, 1, 1, 1]
    # target3 = 0

    list4 = [1]
    target4 = 0

    print(mySolution.search(list1, target1))
    print(mySolution.search(list2, target2))
    # print(mySolution.search(list3, target3))
    print(mySolution.search(list4, target4))

if __name__ == "__main__":
    main()
