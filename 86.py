# -*- coding = utf-8 -*-
# @Time : 8/7/2023 9:40 AM
# @Author : Lauren
# @File : 86.py Partition List 36ms 97.24% 16.38mb 56.67% Two pointers
# @Software : PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: [ListNode], x: int) -> [ListNode]:
        list1 = dummy1 = ListNode()
        list2 = dummy2 = ListNode()
        while head:
            if head.val < x:
                list1.next = head
                list1 = list1.next
            else:
                list2.next = head
                list2 = list2.next
            # 移花接木store next node to temp, including all the
            # nodes behind
            temp = head.next
            # break the current head and head.next, as we only want to
            # connect the current head to list1 / list2
            head.next = None
            # move temp linked list to current head
            head = temp
        list1.next = dummy2.next
        return dummy1.next