# -*- coding = utf-8 -*-
# @Time : 5/11/2023 1:43 PM
# @Author : Lauren
# @File : Node.py
# @Software : PyCharm

class ListNode:
    # initialize the linked list object
     def __init__(self, val=0, next=None):
         # val attribute for the node's value
         self.val = val
         # next attribute for a reference to the next node in the list.
         self.next = next

def main():
    # create three nodes with values 1, 2, and 3
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    # link the nodes together
    node1.next = node2
    node2.next = node3

    # print the values in the linked list
    # initialize current node with node_1
    current = node1
    # print the value of all the non-zero nodes
    while current:
        print(current.val)
        current = current.next

if __name__ == "__main__":
    main()

