# -*- coding = utf-8 -*-
# @Time : 5/14/2023 8:13 PM
# @Author : Lauren
# @File : 35.py
# @Software : PyCharm

# 65ms, 17.13mb
class Solution:
    def searchinsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

def main():
    nums = [1, 3, 5, 6]
    target = 5
    mySolution = Solution()
    print(mySolution.searchinsert(nums, target))

if __name__ == "__main__":
    main()
