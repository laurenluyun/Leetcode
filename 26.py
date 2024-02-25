# -*- coding = utf-8 -*-
# @Time : 5/12/2023 1:34 PM
# @Author : Lauren
# @File : 26.py
# @Software : PyCharm

'''
Remove Duplicates from Sorted Array
'''

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # use [:] to replace elements in place, w/o [:] we are creating a
        # new list object
        nums[:] = sorted(set(nums))
        print("nums",nums)
        return len(nums)

class Solution2:
    def removeDuplicates(self, nums: list) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1


class Solution3:
    def removeDuplicates(self, nums: list) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        print(nums)
        return len(nums)

def main():
    nums_1 = [-1,0,0,0,0,3,3]
    nums_2 = [0,0,1,1,1,2,2,3,3,4]
    my_solution = Solution2()
    print(my_solution.removeDuplicates(nums_1))
    print(my_solution.removeDuplicates(nums_2))

if __name__ == "__main__":
    main()

