# -*- coding = utf-8 -*-
# @Time : 11/2/2023 1:39 PM
# @Author : Lauren
# @File : 18.py
# @Software : PyCharm

# sort + 2 for loops + 2 pointers
# 747 ms 16.3mb
def fourSum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    res = []
    length = len(nums)
    if length < 4:
        return res
    # iterate for the 1st pointer
    for i in range(len(nums) - 3):
        if i >= 1 and nums[i] == nums[i - 1]:
            continue
        # iterate for the 2nd pointer
        for j in range(i+1, len(nums) - 2):
            if j - i >= 2 and nums[j] == nums[j - 1]:
                continue
            l = j + 1
            r = length - 1
            while l < r:
                sum = nums[i] + nums[j] + nums[l] + nums[r]
                if sum == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
    return res


def main():
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    print(fourSum(nums1, target1))
    print(fourSum(nums2, target2))


if __name__ == "__main__":
    main()
