# -*- coding = utf-8 -*-
# @Time : 5/24/2023 3:04 PM
# @Author : Lauren
# @File : 167.py
# @Software : PyCharm
'''
Two Sum II - Input Array Is Sorted (Medium)
因为数组已经排好序，我们可以采用方向相反的双指针来寻找这两个数字，一个初始指向最
小的元素，即数组最左边，向右遍历；一个初始指向最大的元素，即数组最右边，向左遍历。
如果两个指针指向元素的和等于给定值，那么它们就是我们要的结果。如果两个指针指向元
素的和小于给定值，我们把左边的指针右移一位，使得当前的和增加一点。如果两个指针指向元
素的和大于给定值，我们把右边的指针左移一位，使得当前的和减少一点。
122ms, 17,14mb
'''

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start + 1, end + 1]
            elif sum < target:
                start += 1
            else:
                end -= 1


def main():
    mySolution = Solution()
    numbers1 = [2,7,11,15]
    target1 = 9
    numbers2 = [2,3,4]
    target2 = 6
    numbers3 = [-1,0]
    target3 = -1
    print(mySolution.twoSum(numbers1, target1))
    print(mySolution.twoSum(numbers2, target2))
    print(mySolution.twoSum(numbers3, target3))

if __name__ == "__main__":
    main()
