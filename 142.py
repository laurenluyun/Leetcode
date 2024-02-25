# -*- coding = utf-8 -*-
# @Time : 5/26/2023 12:12 PM
# @Author : Lauren
# @File : 142.py
# @Software : PyCharm

'''
Linked list CycleII (Medium)
75ms, 20.5mb
'''

class Solution:
    def detectCycle(self, head: listNode) -> listNode:
        # initialize two pointers, slow and fast, to the head of the linked
        # list
        slow = head
        fast = head

        # move the slower pointer one step and the fast pointer two steps
        # at a time through the linked list until they either meet or the
        # fast point reaches the end of the list.
        # while fast and fast.next are not null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
            # if the pointers meet, there is a cycle in the linked list.
            # Reset the slow pointer to the head of the linked list,
            # and move pointers one step at a time until they meet again. The
            # node where they meet is the starting point of the cycle.
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

            # if the fast pointer reaches the end of the list without
            # meeting the slow pointer, there is no cycle in the linked
            # list, return None.
        return None
