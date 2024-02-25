# -*- coding = utf-8 -*-
# @Time : 5/6/2023 10:47 PM
# @Author : Lauren
# @File : 9.py
# @Software : PyCharm

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(len(s) // 2 + 1):
            if s[i] == s[len(s) - 1 - i]:
                continue
            else:
                return False
        return True


def main():
    my_solution = Solution()
    int_1 = 1
    int_2 = 12
    int_3 = 11
    int_4 = 121
    print(my_solution.isPalindrome(int_1))
    print(my_solution.isPalindrome(int_2))
    print(my_solution.isPalindrome(int_3))
    print(my_solution.isPalindrome(int_4))

if __name__ == "__main__":
    main()

