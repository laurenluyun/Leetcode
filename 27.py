# -*- coding = utf-8 -*-
# @Time : 5/13/2023 10:30 AM
# @Author : Lauren
# @File : 27.py
# @Software : PyCharm
# 58ms
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    mySolution = Solution()
    print(mySolution.removeElement(nums, val))

if __name__ == "__main__":
    main()