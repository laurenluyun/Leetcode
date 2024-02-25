# -*- coding = utf-8 -*-
# @Time : 7/19/2023 9:03 AM
# @Author : Lauren
# @File : 11.py Container with most water
# @Software : PyCharm

# brute force: time limit exceeded
def maxArea(height: list[int]) -> int:
    maxArea = 0
    for l, a in enumerate(height):
        r = len(height) - 1
        while r > l:
            product = (r - l) * min(a, height[r])
            maxArea = max(maxArea, product)
            r -= 1
    return maxArea

# linear time solution O(n) 739ms 44.9%, 29.4mb 28.62%
def maxArea01(height: list[int]) -> int:
    l, maxArea, r, = 0, 0, len(height) - 1
    while r > l:
        product = (r - l) * min(height[l], height[r])
        maxArea = max(maxArea, product)
        # skip the left point when it is lower than the current right pointer
        if height[l] < height[r]:
            l += 1
        # skip the right pointer when it is lower than the left pointer
        else:
            r -= 1
    return maxArea


def main():
    height1 = [1,8,6,2,5,4,8,3,7]
    height2 = [1,1]
    print(maxArea01(height1))
    print(maxArea01(height2))

if __name__ == "__main__":
    main()