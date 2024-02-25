# -*- coding = utf-8 -*-
# @Time : 7/25/2023 9:11 AM
# @Author : Lauren
# @File : 19.py Remove Nth Node from End of List - two pointers O(n)
# @Software : PyCharm

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    37ms, 97.61%, 16.39mb 39.17%
    left and right pointer, to get access to the nth node from end of list, left pointer
    starts at head, right pointer head.next.next, keep traversing the list
    until right pointer reaches the null node, (there's always one node
    between left and right node) the left pointer will be at the nth node
    from end of list
    to get rid of the nth node, we need to find the n - 1 node
    不过注意我们又使用了虚拟头结点的技巧，也是为了防止出现空指针的情况，比如说链表总共有 5 个节点，
    题目就让你删除倒数第 5 个节点，也就是第一个节点，那按照算法逻辑，应该首先找到倒数第 6 个节点。
    但第一个节点前面已经没有节点了，这就会出错。但有了我们虚拟节点 dummy 的存在，就避免了这个问题，能够对这种情况进行正确的删除。
    '''
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # right pointer move first by n nodes
        while n > 0:
            right = right.next
            n -= 1
        # 2 pointers move together, always have 2 points in between
        # when right pointer is reaches null, left pointer is the n - 1th
        # from the end
        while right:
            left = left.next
            right = right.next
        # delete
        left.next = left.next.next
        return dummy.next



def main():
    head1 = [1, 2, 3, 4, 5]
    n1 = 2
    head2 = [1]
    n2 = 1
    mySolution = Solution()
    print(mySolution.removeNthFromEnd(head1, n1))
    print(mySolution.removeNthFromEnd(head2, n2))

if __name__ == "__main__":
    main()
