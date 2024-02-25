# -*- coding = utf-8 -*-
# @Time : 5/10/2023 1:31 PM
# @Author : Lauren
# @File : 20.py
# @Software : PyCharm
'''
每一个括号中不能包含一个未闭合的括号，里层的括号先闭合，再到最外层的括号，需要考虑顺序
'''
class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] == "(" and ")" not in s[i+1:]:
                return False
            elif s[i] == "[" and "]" not in s[i+1:]:
                return False
            elif s[i] == "{" and "}" not in s[i+1:]:
                return False
            else:
                return True

class Solution_1:
    '''
    O(n) for time and memory complexity
    '''
    def isValid(self, s: str) -> bool:
        # hashmap
            d = {'(': ')', '{': '}', '[': ']'}
            stack = []
            for i in s:
                if i in d:  # 1
                    # if the current element is in the key of the dictionary
                    # then push it onto the stack
                    stack.append(i)
                    # if the stack is empty, it means there is no opening
                    # bracket which is in the dict, so return False
                    # or if the respective ending element of the last element
                    # of the stack which should be one of the beginning
                    # brackets of does not equal to the current bracket,
                    # return False
                elif not stack or d[stack.pop()] != i:  # 2
                    # if not stack => not empty => true
                    return False
            # return True if the stack is empty, False otherwise
            return not stack  # 3

def main():
    str_1 = "()"
    str_2 = "()[]{}"
    str_3 = "([)]"
    my_solution = Solution_1()
    print(my_solution.isValid(str_1))
    print(my_solution.isValid(str_2))
    print(my_solution.isValid(str_3))

if __name__ == "__main__":
    main()
