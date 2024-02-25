# -*- coding = utf-8 -*-
# @Time : 7/24/2023 9:53 AM
# @Author : Lauren
# @File : 143.py Reorder List Medium
# linked list, slow & fast pointer
# @Software : PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        we are alternating between the first and the last node
        time complexity: O(n) 107ms, memoryL O(1) 25.92mb
        cut the node into 2 halfs
        merge the two parts - the first half is merged from the beginning,
        the second half is merged from the end, so we have to reverse the
        second half and then merge it with the first half
        """
        # find the middle which is the slow pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # shift the pointer by one
            fast = fast.next.next # shift the pointer by two

        # reverse second half, head is the next node of the middle node
        second = slow.next
        prev = slow.next = None
        while second:
            # first store the next node in a temp
            tmp = second.next
            # re-direct the current node to the previous node
            second.next = prev
            # assign the previous node with the value of current node,
            # be pointed by current (4)
            prev = second
            # current node with the value of next node, pointing to prev(3)
            second = tmp

        # merge two halfs
        # head is the head of the 1st half, prev is the head of the second
        # half
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


def main():
    head1 = [1,2,3,4]
    head2 = [1,2,3,4,5]
    mySolution = Solution()
    print(mySolution.reorderList(head1))
    print(mySolution.reorderList(head2))

if __name__ == "__main__":
    main()


