# -*- coding = utf-8 -*-
# @Time : 8/7/2023 3:36 PM
# @Author : Lauren
# @File : 876.py Middle of the Linked List 37ms, 89.35% 16.18mb, 93.87%
# @Software : PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head:[ListNode]) -> [ListNode]:
        pointer1 = pointer2 = head
        while pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        return pointer1


