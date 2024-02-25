# -*- coding = utf-8 -*-
# @Time : 7/23/2023 9:09 AM
# @Author : Lauren
# @File : 206.py Reverse Linked LIst Easy
# @Software : PyCharm

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(head: list) -> list:
    # pointers: time: O(n) memory:O(1)
    '''
    36ms, 99.37%, 17.82mb
    point the next node to be the previous node
    move the current node to the previous node
    change the current node to be the next node
    '''
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

class Solution:
    def reverseList02(self, head: list) -> list:
        # recursive: time: O(n) memory:O(n)
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

def main():
    head1 = [1,2,3,4,5]
    print(reverseList(head1))

if __name__ == "__main__":
    main()


