# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# Given linked list -- head = [4,5,1,9], which looks like following:
#
#   4 -> 5 -> 1 -> 9
#
# -----------------------
# Example 1:
# -----------------------
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# -----------------------
# Example 2:
# -----------------------
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
#
# ===============
# Note:
# ===============
#
# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next = node.next      # [4,5,1,9] ==> node = 5 and it's next = 1 so, next = node.next = 1 (here we are skipping 5)
        node.val = next.val   # here node.val = next.val means 5 is node and it's next value is 1 so we are setting this node.val = 1
        node.next = next.next # now we move to the next node node.next = next.next here, next.next means 9 is next of 1 so, output of the linkedlist = [4,1,9]
