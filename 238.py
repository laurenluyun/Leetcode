# -*- coding = utf-8 -*-
# @Time : 7/14/2023 8:56 AM
# @Author : Lauren
# @File : 238.py
# @Software : PyCharm
# requirement: O(n) division operation is not allowed
# prefix array, postfix array -> output
# 240MS
def productExceptSelf(nums: list[int]) -> list[int]:
    prefix = postfix = 1
    output = [1] * len(nums)
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]
    for i in range(len(nums)-1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]
    return output

def productExceptSelf01(nums: list[int]) -> list[int]:
    prefix = postfix = 1
    output = [1] * len(nums)
    for i in range(len(nums)):
        output[i] = prefix # note: output[i] is the product of i-1 elements
        prefix *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= postfix
        postfix *= nums[i]

    return output
def main():
    nums1 = [1, 2, 3, 4]
    # nums2 = [-1, 1, 0, -3, 3]
    # print(productExceptSelf(nums1))
    # print(productExceptSelf(nums2))
    print(productExceptSelf01(nums1))

if __name__ == "__main__":
    main()
