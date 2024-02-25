# -*- coding = utf-8 -*-
# @Time : 5/15/2023 5:07 PM
# @Author : Lauren
# @File : 455.py
# @Software : PyCharm

# assign cookies, greedy algo
# 172ms 18.2mb
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g_sorted = sorted(g)
        s_sorted = sorted(s)
        child = 0
        cookie = 0
        # while loop when number of children is less than the length of the
        # list, same for cookie list
        while child < len(g_sorted) and cookie < len(s_sorted):
            # if the current child is fullfilled then child + 1
            if g_sorted[child] <= s_sorted[cookie]:
                child += 1
            # increase the cookie no matter if the current child is
            # fullfilled or not
            cookie += 1
        return child

def main():
    my_solution = Solution()
    g = [1, 2]
    s = [1, 2, 3]
    print(my_solution.findContentChildren(g, s))

if __name__ == "__main__":
    main()