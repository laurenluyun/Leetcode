# -*- coding = utf-8 -*-
# @Time : 12/28/2023 7:18 PM
# @Author : Lauren
# @File : 316.py
# @Software : PyCharm

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        # mantain a counter to store the number of each char size of 256 ASCII
        count = [0] * 256
        for i in range(len(s)):
            count[ord(s[i])] += 1
        # inStack is to tell if the char is in the stack, if already in not
        # append in stack, otherwise not, which avoid duplicates
        inStack = [False] * 256
        for c in s:
            # iterate the list and decrease respective char
            count[ord(c)] -= 1
            # if the char is already in stack, skip to the next loop
            if inStack[ord(c)]:
                continue

            # this loop is to pop element from stack when stack has
            # element and the rightmost element > c, as we want smaller
            # char, so we pop from the rightmsot element
            while len(stack) > 0 and stack[-1] > c:
                # stop popping if there's no such element(rightmost) left
                # in s
                if count[ord(stack[-1])] == 0:
                    break
                # else pop the rightmost element from stack and mark the
                # element not in stack
                inStack[ord(stack.pop())] = False

            # here the char is not in stack, so append it to the stack
            stack.append(c)
            # mark the char is in stack
            inStack[ord(c)] = True
        sb = []
        # append each element in the reverse order of the s as stack is LIFO
        while len(stack) > 0:
            sb.append(stack.pop())
        # reverse the list and convert to string
        return "".join(sb)[::-1]

