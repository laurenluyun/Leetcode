# -*- coding = utf-8 -*-
# @Time : 5/6/2023 11:00 PM
# @Author : Lauren
# @File : 191.py
# @Software : PyCharm

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         n_string = str(n)
#         count = 0
#         for each in n_string:
#             if each == "1":
#                 count += 1
#         return count

class Solution1:
    # O(32) constant => O(1)
    def hammingWeight(self, n: int) -> int:
        res = 0
        # while n != 0
        while n:
            # n % 2 will be 1 if the bit is 1, 0 if the bit is 0
            res += n % 2
            # move the bit to right by 1 or n  / 2 can do the same
            n = n >> 1
        return res
class Solution2:
    # O(number of 1) constant => O(1)
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # n-1 is to subtract 1 from n, logic & is to make sure that
            # the rest of n would stay unchanged for use to do the next
            # round of this statement
            n &= (n - 1)
            res += 1
        return res
def main():
    my_solution = Solution1()
    int_1 = 100000000000000000000000000001011
    int_2 = 100000000000000000000000010000000
    int_3 = 11111111111111111111111111111101
    print(my_solution.hammingWeight(int_1))
    print(my_solution.hammingWeight(int_2))
    print(my_solution.hammingWeight(int_3))

if __name__ == "__main__":
    main()


