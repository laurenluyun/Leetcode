# -*- coding = utf-8 -*-
# @Time : 8/1/2023 1:54 PM
# @Author : Lauren
# @File : 303.py Range Sum Query - Immutable Easy
# sum of prefix
# @Software : PyCharm

class NumArray:
    '''
    70ms, 99.26%, 20.10mb, 20.89% O(1)
    '''
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.preSum = [0] * (len(nums) + 1)

    # search for the sum of the [left, right]
    def sumRange(self, left: int, right: int) -> int:
        # preSum[right] is the sum of prefix of right hence right + 1 to
        # include right, preSum[left] similar, we don't need to deduct left
        # itself but the sum of its prefix
        # set up the sum of the prefix
        for i in range(1, len(self.nums) + 1):
            self.preSum[i] = self.preSum[i - 1] + self.nums[i - 1]
        return self.preSum[right + 1] - self.preSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
def main():
    nums = [-2, 0, 3, -5, 2, -1]
    left1 = 0
    right1 = 2
    left2 = 2
    right2 = 5
    left3 = 0
    right3 = 5
    obj = NumArray(nums)
    param_1 = obj.sumRange(left, right)

