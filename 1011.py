# -*- coding = utf-8 -*-
# @Time : 12/22/2023 2:24 PM
# @Author : Lauren
# @File : 1011.py
# @Software : PyCharm


class Solution:
    # f(x) solves the question: how many days for a conveyor to deliver the
    # weights given its capacity is x, now we want to know the minimum
    # capacity for a conveyor to deliver the goods given certain days
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # the capacity of the conveyor ranges from max(weight) to sum of
        # weight
        left = max(weights)
        right = sum(weights)
        # use binary search to search for the left bound
        while left < right:
            mid = (left + right) // 2
            # if actual days < days needed, capacity is too big, shrink the
            # right side
            if self.f(weights, mid) <= days:
                right = mid # because we need right = sum, so right = mid
                # instead of mid - 1
            else:
                left = mid + 1
        return left


    # when capacity = x, need f(x) days to ship all the goods,
    # f(x) decreases when x increases, below calculates how many days the
    # ship needs to deliver all the goods given its capacity x
    def f(self, weights, x):
        days = 0
        i = 0
        while i < len(weights):
            cap = x
            while i < len(weights):
                if cap < weights[i]:
                    break
                else:
                    cap -= weights[i]
                    i += 1
            days += 1
        return days






def main():
    mySolution = Solution()
    weights1 = [1,2,3,4,5,6,7,8,9,10]
    days1 = 5

    weights2 = [3,2,2,4,1,4]
    days2 = 3

    weights3 = [1,2,3,1,1]
    days3 = 3
    print(mySolution.shipWithinDays(weights1, days1))
    print(mySolution.shipWithinDays(weights2, days2))
    print(mySolution.shipWithinDays(weights3, days3))

if __name__ == "__main__":
    main()
