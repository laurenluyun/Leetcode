# -*- coding = utf-8 -*-
# @Time : 5/21/2023 3:55 PM
# @Author : Lauren
# @File : 122.py
# @Software : PyCharm
'''
Best time to buy and sell stock - Greedy Algo
股票交易题型里比较简单的题目，在不限制交易次数的情况下，怎样可以获得最大利润呢？
72MS 17.5MB
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        start = prices[0]
        profit_total = 0
        for i in range(1, len(prices)):
            profit = 0
            if prices[i] > start:
                profit = prices[i] - start
            start = prices[i]
            profit_total += profit
        return profit_total



def main():
    my_solution = Solution()
    prices1 = [7,1,5,3,6,4]
    prices2 = [1,2,3,4,5]
    prices3 = [7,6,4,3,1]
    print(my_solution.maxProfit(prices1))
    print(my_solution.maxProfit(prices2))
    print(my_solution.maxProfit(prices3))

if __name__ == "__main__":
    main()

