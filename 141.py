# -*- coding = utf-8 -*-
# @Time : 7/25/2023 12:24 PM
# @Author : Lauren
# @File : 141.py Linked List Cycle Easy
# slow and fast pointer
# @Software : PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        '''
        traverse the list , O(n) for time and memory complexity 75ms,
        54.86%,  20.48mb, 62.5%
        two pointers: slow pointer will shift by one node each time,
        the fast pointer will shift by two
        1. if there is no cycle in the list, then the fast pointer will
        reach at null => return false
        2. if there's a cycle, the slow and fast pointer will meet at the
        same node. The fast pointer will always catch up with the slow
        pointer.
        Each interation will close the two pointers by 1 node. they will
        first meet after the n-1 iteration => O(n)
        '''
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

