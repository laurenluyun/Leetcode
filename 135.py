# -*- coding = utf-8 -*-
# @Time : 5/16/2023 5:23 PM
# @Author : Lauren
# @File : 135.py
# @Software : PyCharm
'''
Candy
173ms, 19.2mb
greedy algo
traverse the list twice
'''

class Solution:
    def candy(self, ratings: list[int]) -> int:
        length = len(ratings)
        candy_list =[1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                candy_list[i] = candy_list[i - 1] + 1
        j = length - 1
        while j >= 1:
            if ratings[j] < ratings[j - 1]:
                # 要至少为本身的candy数量
                candy_list[j - 1] = max(candy_list[j - 1], candy_list[j]
                + 1)
            j -= 1
        return sum(candy_list)

def main():
    my_solution = Solution()
    ratings1 = [1, 0, 2]
    ratings2 = [1, 3, 4, 5, 2]
    print(my_solution.candy(ratings1))
    print(my_solution.candy(ratings2))

if __name__ == "__main__":
    main()
