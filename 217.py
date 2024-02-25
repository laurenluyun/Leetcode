# -*- coding = utf-8 -*-
# @Time : 7/11/2023 11:02 PM
# @Author : Lauren
# @File : 217.py
# @Software : PyCharm

# contains duplicate

def containsDuplicate(nums: list[int]) -> bool:
    # time list exceeded
    i = 1
    for each in nums:
        if each in nums[i:]:
            return True
        else:
            i += 1
    return False

# solution: sort + hashset
def containsDuplicate01(nums: list[int]) -> bool:
    # time list exceeded
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


def main():
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate01(nums1))
    print(containsDuplicate01(nums2))
    print(containsDuplicate01(nums3))


if __name__ == "__main__":
    main()


