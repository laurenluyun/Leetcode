# -*- coding = utf-8 -*-
# @Time : 4/26/2023 1:26 PM
# @Author : Lauren
# @File : 1480.py
# @Software : PyCharm

# Time Complexity : O(n)
# Space Complexity : O(n)
# memory 14mb, runtime 43ms
class Solution_0:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum_list = []
        sum = nums[0]
        for index in range(len(nums)):
            if index == 0:
                sum_list.append(nums[0])
            else:
                sum += nums[index]
                sum_list.append(sum)
        return sum_list


# Time Complexity : O(n)
# Space Complexity : O(n)
class Solution_1(object):
    def runningSum(self, nums):
        # Create an output list of size equal to given nums size,
        # each element = 0
        output = [0] * len(nums)
        # Set output[0] = nums[0]...
        output[0] = nums[0]
        # Traverse all elements through the for loop...
        for idx in range(1, len(nums)):
            # Storing the running sum...
            output[idx] = output[idx - 1] + nums[idx]
        return output       # Return the running sum of nums...

def main():
    print([0] * 3)
    input_1 = [1]
    input_2 = [1, 1, 2, 3, 4]
    my_solution = Solution_0()
    print(my_solution.runningSum(input_1))
    print(my_solution.runningSum(input_2))

if __name__ == "__main__":
    main()