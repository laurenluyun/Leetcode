# -*- coding = utf-8 -*-
# @Time : 6/1/2023 5:57 PM
# @Author : Lauren
# @File : 81.py
# @Software : PyCharm
'''
binary search
left, right and mid pointer
69ms 17mb
'''
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex <= rightIndex:
            midIndex = (leftIndex + rightIndex) // 2
            if nums[midIndex] == target:
                return True

            if nums[leftIndex] == nums[midIndex]:
                leftIndex += 1

            # if the mid is in the left portion
            if nums[leftIndex] < nums[midIndex]:
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
        return False

class Solution1:
    def search(self, nums: list[int], target: int) -> bool:
        # Initilize two pointers
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (begin + end)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[end]: # Fail to estimate which side is sorted
                end -= 1  # In worst case: O(n)
            # if the mid is in the right portion
            elif nums[mid] < nums[end]:
                # if the target is less than the mid or is greater than the
                # end, move the pointer to the left
                if target <= nums[mid] or target > nums[end]:
                    end = mid - 1
                # if the target is within the mid and the end, move to the
                # right
                else: # in right side
                    begin = mid + 1
            # if the mid point is in the left portion
            else:
                # if the target is less than the begin or is greater than
                # the mid point, move to the right
                if target < nums[begin] or target >= nums[mid]:
                    begin = mid + 1
                else: # if the target is within the begin and the mid,
                    # move to the left
                    end = mid - 1
        return False

def main():
    mySolution = Solution1()
    list1 = [2,5,6,0,0,1,2]
    target1 = 0

    list2 = [2,5,6,0,0,1,2]
    target2 = 3

    list3 = [1, 0, 1, 1, 1]
    target3 = 0

    list4 = [1]
    target4 = 0

    print(mySolution.search(list1, target1))
    print(mySolution.search(list2, target2))
    print(mySolution.search(list3, target3))
    print(mySolution.search(list4, target4))

if __name__ == "__main__":
    main()
