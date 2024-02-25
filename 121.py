# -*- coding = utf-8 -*-
# @Time : 7/20/2023 11:35 AM
# @Author : Lauren
# @File : 121.py Best Time to Sell and Buy Stock
# Type: sliding window
# @Software : PyCharm

# time limit exceeded
def maxProfit(prices: list[int]) -> int:
    profit = 0
    for l, price in enumerate(prices):
        r =len(prices) - 1
        while l < r:
            if price <= prices[r]:
                difference = prices[r] - price
                profit = max(profit, difference)
            r -= 1
            while l < r and prices[r] <= prices[r + 1]:
                r -= 1
    return profit

'''
sliding window solution: 
memory: O(1) 27.39mb, time O(n) 1065ms
two pointers all start at the beginning of the list, formating a sliding 
window
l = 0, r = 1
if list[r] >  list[l], cal profit, take the maximum, r += 1
else: l = r, skip the window beginning at the lowest point so far
r += 1
'''
def maxProfit01(prices: list[int]) -> int:
    l, profit, r = 0, 0, 1
    while r < len(prices):
        if prices[r] > prices[l]:
            difference = prices[r] - prices[l]
            profit = max(profit, difference)
        else:
            # when the right pointer is less than the left, change the
            # right pointer to be the left pointer
            l = r
        r += 1
    return profit


def main():
    prices1 = [7,1,5,3,6,4]
    prices2 = [7,6,4,3,1]
    prices3 = [3, 3]
    prices4 = [3]

    print(maxProfit01(prices1))
    print(maxProfit01(prices2))
    print(maxProfit01(prices3))
    print(maxProfit01(prices4))

if __name__ == "__main__":
    main()