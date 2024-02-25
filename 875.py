# -*- coding = utf-8 -*-
# @Time : 12/22/2023 4:46 PM
# @Author : Lauren
# @File : 875.py
# @Software : PyCharm

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # find the left bound of k, eating speed ranges from 0 to sum(piles)
        left = 1
        right = sum(piles)
        while left < right:
            mid = (left + right) // 2
            if self.f(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left

    # decide how many hours koko needs to finish all the bananas given
    # eating speed k
    def f(self, piles, k):
        hours = 0
        for i in range(len(piles)):
            hours += piles[i] // k
            if piles[i] % k > 0:
                hours += 1
        return hours

def main():
    mySolution = Solution()
    piles1 = [3, 6, 7, 11]
    h1 = 8

    piles2 = [30, 11, 23, 4, 20]
    h2 = 5

    piles3 = [30,11,23,4,20]
    h3 = 6
    print(mySolution.minEatingSpeed(piles1, h1))
    print(mySolution.minEatingSpeed(piles2, h2))
    print(mySolution.minEatingSpeed(piles3, h3))

if __name__ == "__main__":
    main()
