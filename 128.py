# -*- coding = utf-8 -*-
# @Time : 7/16/2023 10:00 AM
# @Author : Lauren
# @File : 128.py Longest Consecutive Sequence require O(n)
# @Software : PyCharm

'''
465ms 60.31%, 30.74mb, 95.9%, but when use sort O(nlogn)
'''
def longestConsecutive(nums: list[int]) -> int:
    numSorted = sorted(nums)
    p1 = 0
    p2 = length = 1
    res = []

    if len(nums) == 0:
        return 0
    while p2 < len(nums):
        if numSorted[p2] - numSorted[p1] == 1:
            length += 1
        elif numSorted[p2] == numSorted[p1]:
            length += 0
        else:
            res.append(length)
            length = 1
        p1 += 1
        p2 += 1
    res.append(length)
    return max(res)

def longestConsecutive01(nums: list[int]) -> int:
    '''
    O(n)
    2032ms, 39.17%, 31.14mb 48.2%
    '''
    numSet = set(nums)
    longest = 0
    for n in nums:
        #check if it's the start of the sequence, we only pick those start
        # of the sequence to count the length
        if (n-1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

def longestConsecutive02(nums: list[int]) -> int:
    '''
    O(n)
    2032ms, 39.17%, 31.14mb 48.2%
    '''
    numsSet = set(nums)
    longest = 0
    for num in nums:
        # only start with the smallest number
        if not (num - 1) in numsSet:
            length = 0
            while (num + length) in numsSet:
                length += 1
            longest = max(longest, length)
    return longest

def main():
    nums1 = [100,4,200,1,3,2]
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutive02(nums1))
    print(longestConsecutive02(nums2))

if __name__ == "__main__":
    main()
