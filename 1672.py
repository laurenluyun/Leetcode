# -*- coding = utf-8 -*-
# @Time : 4/26/2023 7:12 PM
# @Author : Lauren
# @File : 1672.py
# @Software : PyCharm

# Time complexity
# Space complexity
# memory, runtime
import math
class Solution_0:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        new_list = []
        for each in accounts:
            sum_each = 0
            for element in each:
                sum_each += element
            new_list.append(sum_each)
        return max(new_list)

class Solution_1:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans = 0
        for index in range(len(accounts)):
            curr_sum = sum(accounts[index])
            ans = max(ans, curr_sum)
        return ans

class Solution_2:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(sum(acc) for acc in accounts)

def main():
    input_1 = [[1, 2, 3], [3, 2, 1]]
    input_2 = [[1, 5], [7, 3], [3, 5]]
    input_3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    my_solution = Solution_2()
    print(my_solution.maximumWealth(input_1))
    print(my_solution.maximumWealth(input_2))
    print(my_solution.maximumWealth(input_3))
    # can use sum directly to derive the sum of all the elements of a list
    print(sum([1, 2, 3]))

if __name__ == "__main__":
    main()
