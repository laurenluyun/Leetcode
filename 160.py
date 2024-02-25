# -*- coding = utf-8 -*-
# @Time : 8/7/2023 4:26 PM
# @Author : Lauren
# @File : 160.py Intersection of Two Linked List 2 pointers
# 84ms
# @Software : PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        pointer1 = headA
        pointer2 = headB
        while pointer1 != pointer2:
            if pointer1 == None:
                pointer1 = headB
            else:
                pointer1 = pointer1.next
            if pointer2 == None:
                pointer2 = headA
            else:
                pointer2 = pointer2.next
        # if there is no intersection, will return node None
        return pointer1

