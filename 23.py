# -*- coding = utf-8 -*-
# @Time : 7/26/2023 9:37 AM
# @Author : Lauren
# @File : 23.py Merge k sorted List Hard
# Merge Sort => nlog(k) & Merge two linked list
# 116ms 66.72% 19.99mb 79.49%
# @Software : PyCharm

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[[ListNode]]) -> [ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            # merge sort, compare two adjacent lists each time, merge the
            # original list first
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # check the adjacent list is non-null, merging one non-null
                # list and one null list is perfectly fine
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            # each time the original list is merged, keep merging the list
            # until the list only has one element
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy #拉索
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

