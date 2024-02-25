# -*- coding = utf-8 -*-
# @Time : 5/11/2023 11:53 AM
# @Author : Lauren
# @File : 21.py
# @Software : PyCharm

# 53ms, 16.3MB
# Definition for singly-linked list.
class ListNode:
    # initialize the linked list object
     def __init__(self, val=0, next=None):
         # val attribute for the node's value
         self.val = val
         # next attribute for a reference to the next node in the list.
         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2) -> list:
        # create cur / dummy node with value = 0, next = none
        # we also use cur pointer to keep track of the last node in the
        # merged list
        # Initially, cur points to the dummy node, which is the first node in the merged list
        cur = dummy = ListNode()
        # while both node 1 and node 2 are non-zero
        while list1 and list2:
            # compare the value of the two nodes, and
            # 1. then append the node with the smaller value to the current node
            # 2. then point the current node to the node just appended /
                # assign the current the node with the value of the node just
                # appended
            # 3. then update the node with smaller value with its next node
            if list1.val < list2.val:
                # append the first node to the current node
                cur.next = list1
                # 1. update the first node to be its next node by assignment
                # statement
                # 2. update the cur node to the last node of the merged
                # list，so that the next node could still be appended to the cur node
                # to form a linked node

                list1, cur = list1.next, list1
            else:
                # if the second node is smaller, then append the second
                # node to the current node
                cur.next = list2
                # 1. update the second node to its next node
                # 2. update the cur node to the last node of the
                # merged list, so that the next node could still be
                # appended to the cur node
                list2, cur = list2.next, list2
        # if only one of the node is non-zero
        if list1 or list2:
            # append the non-zero node to the current node
            cur.next = list1 if list1 else list2
        # the updates on cur will also be applied to dummy
        '''
        dummy.next points to the first node of the merged list, while dummy 
        itself points to the dummy node. To provide the head of the merged 
        list as the function output, we return dummy.next, which is the first 
        node of the merged list.
        '''
        return dummy.next

def main():
    list1 = [1, 2, 3]
    list2 = [1, 3, 4]
    my_solution = Solution()
    print(my_solution.mergeTwoLists(list1, list2))


if __name__ == "__main__":
    main()


