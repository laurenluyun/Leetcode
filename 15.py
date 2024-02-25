# -*- coding = utf-8 -*-
# @Time : 7/18/2023 9:57 AM
# @Author : Lauren
# @File : 15.py 3Sum
# @Software : PyCharm

# brute force : exceed time limit
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    point1 = 0
    res = []
    while point1 < len(nums) - 2:
        point2 = point1 + 1
        while point2 < len(nums) - 1:
            point3 = point2 + 1
            while point3 < len(nums):
                sublist = [nums[point1], nums[point2],nums[point3]]
                if sum(sublist) == 0 and sublist not in res:
                    res.append(sublist)
                point3 += 1
            point2 += 1
        point1 += 1
    return res

def threeSum01(nums: list[int]) -> list[list[int]]:
    # to eliminate duplicates, sort the input array O(nlogn)
    # use one loop for pointer1, second loop to solve 2Sum => 2 nested
    # loops => O(n^2) + O(nlogn) => O(n^2) 1294ms 79.75%
    # Memory: O(1) or O(n) depends on implementation of sorting 20.55mb

    # use left and right pointer, and if the sum > 0,
    res = []
    nums.sort()
    # iterate through the index and the value for 1st pointer
    for i, a in enumerate(nums):
        # skip the same value for the 1st pointer
        if i > 0 and a == nums[i - 1]:
            continue
        # below is 2Sum
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                # avoid duplicates again for 2Sum
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res

def threeSum02(nums: list[int]) -> list[list[int]]:
    # 1202ms, 20.48
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        # skip the same nums[i]
        if i >=1 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            # sum must be put into the while loop
            sum = nums[i] + nums[l] + nums[r]
            if sum == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                # skip the next pointer which is the same
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
    return res



def main():
    nums1 = [-1,0,1,2,-1,-4]
    nums2 = [0,1,1]
    nums3 = [0,0,0]
    nums4 = [3,0,-2,-1,1,2]
    print(threeSum02(nums1))
    print(threeSum02(nums2))
    print(threeSum02(nums3))
    print(threeSum02(nums4))



if __name__ == "__main__":
    main()
