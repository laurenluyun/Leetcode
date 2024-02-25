# -*- coding = utf-8 -*-
# @Time : 5/3/2023 7:12 PM
# @Author : Lauren
# @File : 1.py
# @Software : PyCharm

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # list approach, find if the right number is in the remainder of the
# list 359ms, 17.05mb
        # for index in range(len(nums)):
        #     difference = target - nums[index]
        #     list_left = nums[index + 1:]
        #     if difference in list_left:
        #         return [index, (list_left.index(difference) + index + 1)]

        # hashmap approach, val -> index  64ms, 17.54mb
        valToIndex = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in valToIndex:
                return [i, valToIndex[difference]]
            else:
                valToIndex[nums[i]] = i





def main():
    nums_1 = [3, 2, 3]
    target1 = 6
    my_solution = Solution()
    print(my_solution.twoSum(nums_1, target1))

if __name__ == "__main__":
    main()
