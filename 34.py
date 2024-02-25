# -*- coding = utf-8 -*-
# @Time : 6/1/2023 4:19 PM
# @Author : Lauren
# @File : 34.py
# @Software : PyCharm
'''
binary search always have three pointers:
left, right and mid pointer
101ms, 17.9mb
'''
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def search(x):
            '''
            search is to find the first number in the list which is <= the
            target
            lowerboundary: so firstly search for the lowerboundary of target
            higherboundary:search for the higherboundary for target + 1,
            then deduct the result by 1
            '''
            lowerbound, higherbound = 0, len(nums)
            while lowerbound < higherbound:
                mid = (lowerbound + higherbound) // 2
                if nums[mid] < x:
                    lowerbound = mid + 1
                else:
                    higherbound = mid
            return lowerbound

        lowerbound = search(target)
        higherbound = search(target + 1) - 1

        if lowerbound <= higherbound:
            return [lowerbound, higherbound]

        return [-1, -1]

def searchRange1(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    lower_bound = upper_bound = -1
    while right >= left:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            right = mid - 1
    if left >= 0 and left < len(nums) and nums[left] == target:
        lower_bound = left

    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] == target:
            left = mid + 1
    if right >= 0 and right < len(nums) and nums[right] == target:
        upper_bound = right
    return [lower_bound, upper_bound]
def main():
    list1 = [5,7,7,8,8,10]
    target1 = 8

    list2 = [5,7,7,8,8,10]
    target2 = 6

    list3 = []
    target3 = 0
    print(searchRange1(list1, target1))
    print(searchRange1(list2, target2))
    print(searchRange1(list3, target3))

if __name__ == "__main__":
    main()
