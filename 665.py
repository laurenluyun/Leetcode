# -*- coding = utf-8 -*-
# @Time : 5/23/2023 8:00 AM
# @Author : Lauren
# @File : 665.py
# @Software : PyCharm
'''
Non-decreasing Array, Medium, Greedy Algo
197ms, 17.8MB
'''

class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        cnt_violations = 0
        for i in range(1, len(nums)):
            # if the current element is less than the previous one
            if nums[i] < nums[i - 1]:
                # return false if count = 1
                if cnt_violations == 1:
                    return False
                # count += 1
                cnt_violations += 1
                # if the current element is also less than the element at [i -
                # 2], set the element to be the previous element
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
        return True








def main():
    mySolution = Solution()
    nums1 = [4,2,3] # 拿掉max
    nums2 = [4,2,1]
    nums3 = [3, 4, 2, 3]
    nums4 = [5, 7, 1, 8] # 拿掉min
    print(mySolution.checkPossibility(nums1))
    print(mySolution.checkPossibility(nums2))
    print(mySolution.checkPossibility(nums3))
    print(mySolution.checkPossibility(nums4))

if __name__ == "__main__":
    main()