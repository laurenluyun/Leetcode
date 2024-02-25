# -*- coding = utf-8 -*-
# @Time : 1/2/2024 12:24 PM
# @Author : Lauren
# @File : 224.py
# @Software : PyCharm
import collections

# can replace stack with lst
class Solution:
    def calculate(self, s: str) -> int:
        # below s is type deque
        def helper(s) -> int:
            stack = []
            sign = '+'
            num = 0
            # pop each char of the string from left to right
            while len(s) > 0:
                # s is deque
                c = s.popleft()
                # handle digits
                if c.isdigit():
                    num = num * 10 + int(c)
                # start recursion when encounters (
                if c == '(':
                    # call the helper start recursion
                    num = helper(s)
                # handle the operators
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / float(num))
                    num = 0
                    sign = c
                # return if encounter )
                if c == ')':
                    break
            return sum(stack)
        # creates a double-ended queue (deque) object from an iterable
        return helper(collections.deque(s))









